---
title: "Create lambda to get app_details data"
date: "2025-09-11"
weight: 1
chapter: false
pre: " <b> 4.1 </b> "
---

#### Create lambda to collect app_details data

1. Access Lambda Function service

   - Select **Function**
   - Select **Create function**
   - Name the function **crawl-app-details-maket-chplay**
   - Runtime select **Python3.12**
   - Role: Select a role with sufficient permissions :>

2. Add layer for lambda
   - Scroll down to the bottom and select: **Add a layer**

![Create VPC](/images/2/9.png?featherlight=false&width=90pc)

   - Select **Custom layers**
   - Select **google_play_scrape**

![Create VPC](/images/2/10.png?featherlight=false&width=90pc)

3. Add code to lambda:

```python
import json
import boto3
import datetime
from google_play_scraper import app

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
        "com.edupia.app.english.kid",
        "com.facebook.katana",
        "com.zhiliaoapp.musically"
    ]

    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    crawled_at = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    results = []

    for package_name in package_list:
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

        results.append({
            "package_name": package_name,
            "detail_file": detail_key
        })

    return {
        "status": "ok",
        "results": results
    }
```

⇒ Each time the code runs, it will get app_details data that changes daily