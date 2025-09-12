---
title : "Tạo bảng trong dynamodb"
date :  "2025-09-11" 
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---

#### Tạo bảng trong DynamoDB

1. Tại giao diện console, tìm kiếm ```DynamoDB``` 

![Create VPC](/images/5-Dynamo/1.png?featherlight=false&width=90pc)

2. Tiến hành tạo bảng:
 - Chọn **Table** 
 - Chọn **Create Table**

![Create VPC](/images/5-Dynamo/2.png?featherlight=false&width=90pc)

3. Điền các thông tin cho bảng:
 - Table name: ```Spend-me```
 - Partition key: ```id```, kiểu dữ liệu **String**
 - Sort key: ```spend```, kiểu dữ liệu **Number**

![Create VPC](/images/5-Dynamo/3.png?featherlight=false&width=90pc)

{{% notice note %}}
Ta không cần phải tạo hết các cột cần thiết mà chỉ cần tạo partition key và sort key 
{{% /notice %}}

4. Click **Create Table** để tiến hành tạo bảng

![Create VPC](/images/5-Dynamo/4.png?featherlight=false&width=90pc)


5. Sau một lúc thì bảng tạo thành cộng với trạng thái **Active**

![Create VPC](/images/5-Dynamo/5.png?featherlight=false&width=90pc)

6. Xem dữ liệu trong bảng:
 - Quay lại giao diện **DynamoDB** chọn **Explore items**
 - Chọn bảng **Spend-me**

![Create VPC](/images/5-Dynamo/6.png?featherlight=false&width=90pc)


{{% notice note %}}
Trên là một số dữ liệu mình đã thêm vào từ trước
{{% /notice %}}





<!-- #### Nội dung 

1. [Lấy mật khẩu ứng dụng Gmail](4.1-createec2/)
2. [Trích xuất thông tin file json](4.2-connectec2/)
3. [Thêm code vào Lambda Function](4.3-natgateway/)
<!-- 4. [Sử dụng Reachability Analyzer](4.4.-createreachabilityanalyzer/)
5. [Tạo EC2 Instance Connect Endpoint](4.5-EICEndpoint/) --> -->