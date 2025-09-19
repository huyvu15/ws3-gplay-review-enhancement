---
title : "Create Lambda to collect app_reviews data"
date :  "2025-09-11" 
weight : 2
chapter : false
pre : " <b> 4.2 </b> "
---

#### Create Lambda to collect app_review data

1. Go to the **Lambda Function** service

- Select **Function**
- Select **Create function**
- Set the function name to **crawl-review-maker-chplay**
- Runtime: **Python3.12**
- Role: Choose a role with sufficient permissions

2. Add a layer to the Lambda
- Scroll down and select: **Add a layer**

![Create VPC](/images/2/9.png?featherlight=false&width=90pc)

- Choose **Custom layers**
- Select **google_play_scrape**

![Create VPC](/images/2/10.png?featherlight=false&width=90pc)

3. Add the following code to Lambda:

```python
import json
import boto3
import datetime
from google_play_scraper import app, reviews_all, Sort

s3 = boto3.client("s3")
BUCKET = "glutisify-datalake"

def save_to_s3(bucket, key, data):
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=data.encode("utf-8"),
        ContentType="application/json"
    )
    print(f"Saved to s3://{bucket}/{key}")

def lambda_handler(event, context):
    package_list = [
        "com.lumina.wallpapers",
        "com.b_lam.resplash",
        "com.pashapuma.pix.wallpapers",
        "com.sspai.cuto.android",
        "com.wallpaperscraft.changer"
    ]

    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    crawled_at = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    days = 7
    start_date = datetime.datetime.utcnow() - datetime.timedelta(days=days)

    results = []

    for package_name in package_list:
        # ---- Crawl App Detail ----
        app_detail = app(package_name, lang="en", country="us")

        if "comments" in app_detail:
            del app_detail["comments"]

        app_detail_record = {
            **app_detail,
            "package_name": package_name,
            "url": f"https://play.google.com/store/apps/details?id={package_name}",
            "crawled_at": crawled_at
        }

        detail_key = f"chplay/app_details/{package_name}/{today}.json"
        save_to_s3(BUCKET, detail_key, json.dumps(app_detail_record, ensure_ascii=False))

        # ---- Crawl Reviews (fetch all and stop when encountering reviews older than 7 days) ----
        all_reviews = reviews_all(
            package_name,
            lang="en",
            country="us",
            sort=Sort.NEWEST
        )

        review_lines = []
        for r in all_reviews:
            review_date = r.get("at")
            if not review_date:
                continue

            if review_date < start_date:
                # Stop if review is older than 7 days
                break

            review_obj = {
                "package_name": package_name,
                "app_title": app_detail.get("title"),
                "url": f"https://play.google.com/store/apps/details?id={package_name}",
                "reviewId": r.get("reviewId"),
                "userName": r.get("userName"),
                "userImage": r.get("userImage"),
                "content": r.get("content"),
                "score": r.get("score"),
                "thumbsUpCount": r.get("thumbsUpCount"),
                "reviewCreatedVersion": r.get("reviewCreatedVersion"),
                "at": review_date.strftime("%Y-%m-%d %H:%M:%S"),
                "replyContent": r.get("replyContent"),
                "repliedAt": r.get("repliedAt").strftime("%Y-%m-%d %H:%M:%S") if r.get("repliedAt") else None,
                "appVersion": r.get("appVersion"),
                "crawled_at": crawled_at
            }
            review_lines.append(json.dumps(review_obj, ensure_ascii=False))

        reviews_key = f"chplay/app_reviews/{package_name}/{today}.json"
        save_to_s3(BUCKET, reviews_key, "\n".join(review_lines))

        results.append({
            "package_name": package_name,
            "detail_file": detail_key,
            "reviews_file": reviews_key,
            "total_reviews": len(review_lines)
        })

    return {
        "status": "ok",
        "results": results
    }


👉 Every time this Lambda is executed, it will fetch weekly app_reviews data.
Fetching weekly data is suitable because most apps have fewer reviews if they have been released for a long time.

Initially, you should collect data from around 1–2 years back to support more comprehensive analysis.




