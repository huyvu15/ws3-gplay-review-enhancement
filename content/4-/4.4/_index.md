---
title : "Lập lịch chạy định kỳ với EventBridge"
date :  "2025-09-11" 
weight : 4
chapter : false
pre : " <b> 4.4 </b> "
---


### Lập lịch chạy định kỳ với EventBridge

Mọi thứ xong xuôi, tuy nhiên dữ liệu chỉ đến thời điểm hiện tại. Để hệ thống hoạt động và xử lý liên tục và luôn cập nhập dữ liệu mới nhất, ta cần các service để lập lịch và kích hoạt

#### Với app_details

1. Truy cập EventBridge


![Create VPC](/images/4/1.png?featherlight=false&width=90pc)

2. Chọn **Schema**
- Chọn **Create Schema**

![Create VPC](/images/4/2.png?featherlight=false&width=90pc)

3. Điền các thông tin:
- Schedule name: ```daily_chplay_app_details``

![Create VPC](/images/4/3.png?featherlight=false&width=90pc)

4. Set Cron time
- Chọn **Cron-based schedule**
- Chọn ```0 6 * * *```: chạy lúc 6h mỗi ngày
- Tại **Flexible time window** chọn **off**
- Chọn Next

![Create VPC](/images/4/4.png?featherlight=false&width=90pc)

Chú ý: **Flexible time window** là thời gian trẻ khi chạy job, nếu chọn 5p thì thời gian chạy job sẽ +5p nữa mới bắt đầu

5. Phần **Select target**:
- Chọn **AWS Lambda**
- Chọn Lambda function ```crawl-app-details-maket-chplay```

![Create VPC](/images/4/5.png?featherlight=false&width=90pc)

6. Chọn **Next**

![Create VPC](/images/4/6.png?featherlight=false&width=90pc)

7. Phần **setting** tiếp:
- Review lại 1 lượt
- Kéo xuống cuối
- Chọn **Use existing role**
- Chọn role đã tạo trước đó: ```1-role-d4jxk5zk```
- Chọn **Next**
![Create VPC](/images/4/7.png?featherlight=false&width=90pc)

8. Review and create schedule
- Chọn **Create schdule**

![Create VPC](/images/4/0.png?featherlight=false&width=90pc)



#### Với app_reviews

1. Phần detail
- Schedule name: ```weekly_chplay_app_reviews```
- Chọn **Recurring schedule**

![Create VPC](/images/4/8.png?featherlight=false&width=90pc)

2. Set Cron time
- Chọn **Cron-based schedule**
- Chọn ```15 6 */7 * *```: chạy lúc 6h15 ngày t8 mỗi tuần
- Tại **Flexible time window** chọn **off**
- Chọn Next

![Create VPC](/images/4/9.png?featherlight=false&width=90pc)

3. Phần **Select target**:
- Chọn **AWS Lambda**
- Chọn Lambda function ```crawl-review-maket-chplay``` 

![Create VPC](/images/4/10.png?featherlight=false&width=90pc)

4. Chọn **Next**

![Create VPC](/images/4/11.png?featherlight=false&width=90pc)

5. Phần **setting** tiếp:
- Review lại 1 lượt
- Kéo xuống cuối
- Chọn **Use existing role**
- Chọn role đã tạo trước đó: ```1-role-d4jxk5zk```
- Chọn **Next**
![Create VPC](/images/4/7.png?featherlight=false&width=90pc)

6. Review and create schedule

- Chọn **Create schdule**

![Create VPC](/images/4/0.png?featherlight=false&width=90pc)


=> Làm tương tự với job triggle lambda job xử lý từ model setiment

Với EventBridge, chúng ta đã thiết lập thành công các lịch chạy định kỳ cho cả app_details và app_reviews, đồng thời có thể mở rộng tương tự cho các job khác như sentiment analysis. Việc lập lịch này giúp hệ thống:

- Tự động hóa quy trình crawl dữ liệu, không cần thao tác thủ công.

- Đảm bảo liên tục cập nhật dữ liệu mới nhất, duy trì tính chính xác và kịp thời.

- Dễ dàng mở rộng cho nhiều tác vụ khác trong pipeline dữ liệu.

Nhờ đó, toàn bộ luồng xử lý dữ liệu trở nên chủ động, ổn định và có khả năng vận hành dài hạn. Đây chính là một trong những bước quan trọng để xây dựng hệ thống phân tích dữ liệu tự động và thông minh hơn.