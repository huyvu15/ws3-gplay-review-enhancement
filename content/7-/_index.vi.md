---
title : "Dọn dẹp tài nguyên"
date :  "2025-09-11" 
weight : 7
chapter : false
pre : " <b> 7. </b> "
---
#### Dọn dẹp tài nguyên

Trong bài lab này chúng ta đã sử dụng các dịch vụ S3, Lambda Function, QuickSight, Glue Job, Sagemaker AI. Các dịch vụ này đều có chi phí khá là rẻ và free cho tài khoản 12 tháng nên ko cần phải xóa tài nguyên.  

Nếu vẫn muốn xóa thì đây là lần lượt các bước:

##### Xóa S3 Bucket
Vào S3 chọn bucket và chọn **glutisify-datalake** và chọn Empty. sau đó chọn **Delete** làm theo các hiển thị tiếp theo để xóa.


##### Xóa Lambda function
Vào Lambda function chọn function chọn **run-sentiment-app-review-batch-transform**, **crawl-app-details-maket-chplay**, **crawl-review-maker-chplay** và chọn **Actions** chọn **Delete** để xóa.


##### Xóa model trên Sagemaker AI
Truy cập vào giao diện Sagemaker AI, chọn model và xóa model đã tạo để tránh phát sinh chi phí

##### Xóa schedule EventBridge
Truy cập giao diện EventBridge 


##### Xóa tài khoản QuickSight

1. Truy cập giao diện QuickSight, tại phần cài đặt
- Chọn **Account settings**
- Chọn **Manage**

![Create VPC](/images/6/23.png?featherlight=false&width=90pc)


2. Tắt **Account termination protection is of**
- Type: ```confirm```
- Chọn **Delete account**

![Create VPC](/images/6/24.png?featherlight=false&width=90pc)




