---
title : "Create S3 Bucket"
date :  "2025-09-11" 
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---

#### Create S3 Bucket

1. Go to the **AWS Management Console**

   - Search for **S3**  
   - Select **Bucket**  
   - Click **Create Bucket**  

![Create VPC](/images/3-Prerequiste/3.1-Create_S3_bucket/1.png?featherlight=false&width=90pc)

2. Enter the bucket name as ```glutisify-datalake```

![Create VPC](/images/3-Prerequiste/3.1-Create_S3_bucket/2.png?featherlight=false&width=90pc)

{{% notice warning %}}
The bucket name must be unique and cannot duplicate any existing bucket names.
{{% /notice %}}

3. Click **Create Bucket**

![Create VPC](/images/3-Prerequiste/3.1-Create_S3_bucket/3.png?featherlight=false&width=90pc)

{{% notice warning %}}
You can choose your own bucket name if you prefer!
{{% /notice %}}

#### Create via CLI
You can also quickly create it using the following CLI command:
```bash
aws s3api create-bucket \
  --bucket glutisify-datalake \
  --region ap-southeast-1 \
  --create-bucket-configuration LocationConstraint=ap-southeast-1
