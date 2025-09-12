---
title : "Tạo S3 Bucket"
date :  "2025-09-11" 
weight : 2 
chapter : false
pre : " <b> 2.1 </b> "
---

#### Tạo S3 Bucket

1. Truy cập giao diện **AWS Management Console**

   - Tìm **S3**
   - Chọn **Bucket**
   - Chọn **Create Bucket**


![Create VPC](/images/3-Prerequiste/3.1-Create_S3_bucket/1.png?featherlight=false&width=90pc)

2. Điền tên bucket là ```bottele```

![Create VPC](/images/3-Prerequiste/3.1-Create_S3_bucket/2.png?featherlight=false&width=90pc)


{{% notice warning %}}
Tên Bucket phải là duy nhất và không được trùng với tên các bucket đã có.
{{% /notice %}}
3. Chọn **Create Bucket**

![Create VPC](/images/3-Prerequiste/3.1-Create_S3_bucket/3.png?featherlight=false&width=90pc)


#### Tạo trên CLI
Mọi người có thể thực hiện nhanh chóng hơn bằng lệnh cli sau:
```bash
aws s3api create-bucket \
  --bucket glutisify-datalake \
  --region ap-southeast-1 \
  --create-bucket-configuration LocationConstraint=ap-southeast-1
```

