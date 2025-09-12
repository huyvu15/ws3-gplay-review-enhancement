---
title : "Export to S3"
date :  "2025-09-11" 
weight : 4
chapter : false
pre : " <b> 6.4 </b> "
---


#### Export to S3

{{% notice note %}}
Sau một thời gian dài sử dụng chatbot (1 y or hơn) bạn có thể đẩy dữ liệu của mình ra S3 để lưu trữ. Hoặc trong trường hợp muốn xóa chatbot và các tài nguyên liên quan.
{{% /notice %}}

1. Tại giao diện DynamoDB 
    - Chọn **Export to S3** 
    - Chọn **Export to S3**
![Create VPC](/images/6/6.4/1.png?featherlight=false&width=90pc)

2. Điền các thông tin export
 - Source table: ```Spend-me```
 - Destination: ```S3://bottele```
 - Chọn **Export**
![Create VPC](/images/6/6.4/2.png?featherlight=false&width=90pc)

![Create VPC](/images/6/6.4/3.png?featherlight=false&width=90pc)

3. Quá trình export bắt đầu

![Create VPC](/images/6/6.4/4.png?featherlight=false&width=90pc)

4. Kiểm tra dữ liệu export trong S3

![Create VPC](/images/6/6.4/5.png?featherlight=false&width=90pc)

![Create VPC](/images/6/6.4/6.png?featherlight=false&width=90pc)

![Create VPC](/images/6/6.4/7.png?featherlight=false&width=90pc)

5. Dữ liệu chi tiêu cá nhân được tải về dưới dạng json

![Create VPC](/images/6/6.4/8.png?featherlight=false&width=90pc)








