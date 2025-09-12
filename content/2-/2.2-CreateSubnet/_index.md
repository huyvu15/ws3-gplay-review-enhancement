---
title : "Tạo Lambda Function"
date :  "2025-09-11" 
weight : 2 
chapter : false
pre : " <b> 2.2 </b> "
---

#### Tạo Lambda Function

1. Trong giao diện **AWS Management Console**

   - Chọn **Lambda**

![Create VPC](/images/3-Prerequiste/3.2-lambda/0.png?featherlight=false&width=90pc)

2. Tại function. Chọn **Create function**
![Create VPC](/images/3-Prerequiste/3.2-lambda/1.png?featherlight=false&width=90pc)

3. Đặt tên function là ```BotTele```
   - Để verion 3.10

![Create VPC](/images/3-Prerequiste/3.2-lambda/2.png?featherlight=false&width=90pc)

4. Chọn **Create function**

![Create VPC](/images/3-Prerequiste/3.2-lambda/3.png?featherlight=false&width=90pc)

5. Tăng timeout cho function
   - Click vào function vừa tạo ```BotTele```
   - Tại giao diện function chọn **Configurations**
   - Chọn **General Configurations**
   - Tiếp tục chọn **Edit** 

![Create VPC](/images/3-Prerequiste/3.2-lambda/4.png?featherlight=false&width=90pc)

6. Đặt description là ```increase timeout```
   - Chỉnh timeout lên 1p
![Create VPC](/images/3-Prerequiste/3.2-lambda/5.png?featherlight=false&width=90pc)

7. Nhấn **Save**

![Create VPC](/images/3-Prerequiste/3.2-lambda/6.png?featherlight=false&width=90pc)

8. Cấu hình quyền cho **Lambda**. Tại giao diện **lambda function**
   - Chọn **Configuration**
   - Chọn **Permissons**
   - Click vào đường dẫn dưới **Role name**
![Create VPC](/images/3-Prerequiste/3.2-lambda/7.png?featherlight=false&width=90pc)

9. Tại giao diện **IAM**
   - Chọn **Role**
   - Chọn **Add Permission**

![Create VPC](/images/3-Prerequiste/3.2-lambda/8.png?featherlight=false&width=90pc)

10. Tìm role **Tìm role **AmazonS3FullAccess**

![Create VPC](/images/3-Prerequiste/3.2-lambda/9.png?featherlight=false&width=90pc)

11. Tìm role **AmazonDynamoDBFullAccess**
   - Chọn **Add Permission**

![Create VPC](/images/3-Prerequiste/3.2-lambda/10.png?featherlight=false&width=90pc)


{{% notice tip %}}
Do đây chỉ là một bài workshop đơn giản nên chúng ta sẽ cấu hình lỏng cho lambda bằng các quyền truy cập mạnh nhất (Full Access)
{{% /notice %}}




