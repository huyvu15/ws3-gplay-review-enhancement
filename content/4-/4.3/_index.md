---
title: "Create lambda to trigger data processing module"
date: "2025-09-11"
weight: 3
chapter: false
pre: " <b> 4.3 </b> "
---

#### Create lambda to collect app_review data

1. Access Lambda Function service

   - Select **Function**
   - Select **Create function**
   - Name the function **run-sentiment-app-review-batch-transform**
   - Runtime select **Python3.12**
   - Role: Select a role with sufficient permissions :>

2. Add code to lambda:

```python
import json
import boto3
import urllib.parse
import time

MODEL_NAME = "distilbert-sst2-fixed-v5"
INPUT_BUCKET = "glutisify-datalake"
OUTPUT_BUCKET = "glutisify-datalake"
INPUT_PREFIX = "chplay/app_reviews/com.facebook.katana/"
OUTPUT_PREFIX = "chplay-gold/app_reviews/com.facebook.katana/"

sagemaker = boto3.client("sagemaker")
s3 = boto3.client("s3")


def create_batch_job(input_uri, filename):
    """Create batch transform job with standard configuration for JSON Lines."""
    file_date = filename.replace(".json", "")
    job_name = f"{MODEL_NAME}-batch-{file_date}-{int(time.time())}"

    response = sagemaker.create_transform_job(
        TransformJobName=job_name,
        ModelName=MODEL_NAME,
        MaxConcurrentTransforms=1,
        MaxPayloadInMB=6,
        BatchStrategy="SingleRecord",
        TransformInput={
            "DataSource": {"S3DataSource": {"S3DataType": "S3Prefix", "S3Uri": input_uri}},
            "ContentType": "application/jsonlines",
            "SplitType": "Line"
        },
        TransformOutput={
            "S3OutputPath": f"s3://{OUTPUT_BUCKET}/{OUTPUT_PREFIX}",
            "Accept": "application/jsonlines",
            "AssembleWith": "Line"
        },
        TransformResources={"InstanceType": "ml.m5.large", "InstanceCount": 1},
    )

    return {
        "jobName": job_name,
        "jobArn": response["TransformJobArn"],
    }


def process_file(bucket, key):
    """Check and process a file from S3."""
    filename = key.split("/")[-1]
    
    if not filename.endswith(".json"):
        return None

    input_uri = f"s3://{bucket}/{key}"
    
    output_key = f"{OUTPUT_PREFIX}{filename}.out"

    try:
        s3.head_object(Bucket=OUTPUT_BUCKET, Key=output_key)
        return None
    except s3.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            return create_batch_job(input_uri, filename)
        else:
            print(f"Error checking S3: {e}")
            raise

def lambda_handler(event, context):
    """Entry point: Process S3 trigger or run manually."""
    try:
        jobs = []
        if "Records" in event:
            print("S3 Event trigger mode.")
            for record in event["Records"]:
                bucket = record["s3"]["bucket"]["name"]
                key = urllib.parse.unquote_plus(record["s3"]["object"]["key"])
                if bucket == INPUT_BUCKET and key.startswith(INPUT_PREFIX):
                    job = process_file(bucket, key)
                    if job:
                        jobs.append(job)

        else:
            print("Manual run mode.")
            response = s3.list_objects_v2(Bucket=INPUT_BUCKET, Prefix=INPUT_PREFIX)
            for obj in response.get("Contents", []):
                job = process_file(INPUT_BUCKET, obj["Key"])
                if job:
                    jobs.append(job)

        return {
            "statusCode": 200,
            "body": json.dumps(
                {"message": f"{len(jobs)} job(s) created", "jobs": jobs}, ensure_ascii=False
            ),
        }

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
```

⇒ Each time the code runs, it will call a batch transform job on SageMaker AI to process the crawled review data