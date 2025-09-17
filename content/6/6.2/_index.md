---
title : "Tạo báo cáo trên QuickSight"
date :  "2025-09-11" 
weight : 2
chapter : false
pre : " <b> 6.2 </b> "
---


#### Tạo báo cáo trên QuickSight

1. Tìm kiếm service QuickSight
![Create VPC](/images/6/1.png?featherlight=false&width=90pc)

2. Đăng ký một tài khoản người dùng mới
![Create VPC](/images/6/2.png?featherlight=false&width=90pc)

3. Điền đầy đủ thông tin
![Create VPC](/images/6/3.png?featherlight=false&width=90pc)

4. Chọn region Singapo và Tích chọn Athena
![Create VPC](/images/6/4.png?featherlight=false&width=90pc)

5. Bỏ chọn **Add Pixel-Pefect-Report**
- Chọn **Finish**
![Create VPC](/images/6/5.png?featherlight=false&width=90pc)

6. Đợi tài khoản được tạo
![Create VPC](/images/6/6.png?featherlight=false&width=90pc)

7. Giao diện ban đầu của QuickSight
![Create VPC](/images/6/7.png?featherlight=false&width=90pc)


8. Chọn **Dataset**
- Chọn **New dataset**

![Create VPC](/images/6/8.png?featherlight=false&width=90pc)

9. Chọn Athena

![Create VPC](/images/6/9.png?featherlight=false&width=90pc)

10.  Điền tên cho source ```chplay-app-data-rating```


![Create VPC](/images/6/11.png?featherlight=false&width=90pc)

11. Chọn database **chplay-gold**
- Chọn table **app_reviews**

![Create VPC](/images/6/12.png?featherlight=false&width=90pc)

12. Tương tự chọn table **app_details**
![Create VPC](/images/6/13.png?featherlight=false&width=90pc)

13. Trực quan 2 bảng:

![Create VPC](/images/6/20.png?featherlight=false&width=90pc)
![Create VPC](/images/6/21.png?featherlight=false&width=90pc)



14. Tại giao diện QuickSight
- Chọn **Analyses**
- Chọn **New analysis**

![Create VPC](/images/6/22.png?featherlight=false&width=90pc)


15. Kéo thả các dashboad, dưới đây là các ví dụ chart bạn có thể tạo

**App_details**

![Create VPC](/images/6/14.png?featherlight=false&width=90pc)

**App_reviews**

![Create VPC](/images/6/15.png?featherlight=false&width=90pc)

![Create VPC](/images/6/16.png?featherlight=false&width=90pc)

![Create VPC](/images/6/19.png?featherlight=false&width=90pc)

![Create VPC](/images/6/18.png?featherlight=false&width=90pc)
