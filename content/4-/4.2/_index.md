---
title : "Tạo lambda lấy data app_reviews"
date :  "2025-09-11" 
weight : 2
chapter : false
pre : " <b> 4.2 </b> "
---




#### Tạo lambda thu thập dữ liệu app_review

1. Truy cập service Lambda Function

- Chọn **Funtion**
- Chọn **Create funtion**
- Đặt tên function là **crawl-review-maker-chplay**
- Runtime chọn **Python3.12**
- Role: Chọn role đủ quyền :>

2. Add layer cho lambda
- Kéo xuống cuối chọn: **Add a layer** 

![Create VPC](/images/2/9.png?featherlight=false&width=90pc)

- Chọn **Custum layers**
- Chọn **google_play_scrape**

![Create VPC](/images/2/10.png?featherlight=false&width=90pc)



3. Thêm code vào lambda:


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

    days = 120
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

        # ---- Crawl Reviews (lấy toàn bộ và dừng khi gặp review cũ hơn 7 ngày) ----
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
                # Nếu gặp review cũ hơn 7 ngày thì dừng luôn
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
```

=> Mỗi khi run code nó sẽ lấy dữ liệu app_details thay đổi theo từng tuần, lấy theo tuần do thông thường app sẽ ít review nếu đã release lâu ngày.






