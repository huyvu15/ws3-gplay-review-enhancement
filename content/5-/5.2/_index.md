---
title : "Tạo crawler cho layer Chplay-gold"
date :  "2025-09-11" 
weight : 2
chapter : false
pre : " <b> 5.2  </b> "
---


#### Tạo crawler cho layer gold

Để nhanh gọn và tập chung thì mọi người tọa crawl chính cho layer gold layer, còn lại mọi người làm tương tự nha!

1. Truy cập giao diện **AWS Glue**

- Chọn **Crawlers**
- Chọn **Create crawler**


![Create VPC](/images/5/1.png?featherlight=false&width=90pc)

2. Nhập:
- Name: ```chplay-gold```
- Description: ```Data after processed```
- Chọn **Next**

![Create VPC](/images/5/2.png?featherlight=false&width=90pc)

3. Chọn **Add a data source**
- Chọn đúng thư mục s3: ```chplay-gold```
- Chọn **Next**

![Create VPC](/images/5/3.png?featherlight=false&width=90pc)

4. Chọn IAM role phù hợp
- Chọn **Next**

![Create VPC](/images/5/4.png?featherlight=false&width=90pc)

5. Từ giao diện **AWS Glue**
- Chọn **Databases**
- Chọn **Create database**
- Name: ```chplay-gold```
- Chọn **Create database**

![Create VPC](/images/5/5.png?featherlight=false&width=90pc)

6. Phần set Output
- Chọn Target database: ```chplay-gold```
- Chọn **Next**

![Create VPC](/images/5/6.png?featherlight=false&width=90pc)


Lưu ý:

{{% notice note %}}
Có thể tự chọn phân cấp thư mục bằng mục prefix
{{% /notice %}}


7. Review lại một lượt



![Create VPC](/images/5/7.png?featherlight=false&width=90pc)


8. Nhận **Run crawler**

![Create VPC](/images/5/8.png?featherlight=false&width=90pc)

=> Lúc này AWS Glue Crawler đã tạo catalog cho 2 bảng app_details, app_reviews





