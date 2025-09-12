---
title : "Webhook"
date :  "2025-09-11" 
weight : 2 
chapter : false
pre : " <b> 1.2 </b> "
---

#### Webhook

![Route Tables](/images/1-Introduce/webhook1.webp?featherlight=false&width=30pc)



Webhook là một cách để các ứng dụng web nhận thông tin theo thời gian thực. Khi sự kiện xảy ra tại một hệ thống, webhook sẽ gửi dữ liệu tự động tới URL khác thông qua một HTTP request. Điều này cho phép hệ thống phản ứng ngay lập tức với các thay đổi dữ liệu hoặc sự kiện mà không cần phải kiểm tra dữ liệu định kỳ.

![Route Tables](/images/1-Introduce/webhook2.webp?featherlight=false&width=30pc)


Cách hoạt động của webhook tương tự như một mạch phản hồi: khi có tín hiệu đầu vào (sự kiện), mạch này sẽ phát tín hiệu đầu ra (HTTP request) ngay lập tức đến điểm cuối đã cấu hình sẵn. Điều này hữu ích trong các ứng dụng mà bạn cần cập nhật dữ liệu liên tục và nhanh chóng như thông báo, đồng bộ hóa dữ liệu giữa các dịch vụ, hay tự động hóa các quy trình làm việc.

Khi một sự kiện xảy ra trong ứng dụng, webhook sẽ giúp ứng dụng khác biết về sự kiện đó và thực hiện các hành động cần thiết. Khi một sự kiện xảy ra trong ứng dụng, nó sẽ gửi một HTTP request đến một URL được chỉ định trước đó được gọi là endpoint, để thông báo cho ứng dụng kia về sự kiến đó


**Ví dụ,** bạn có thể cấu hình một webhook trong hệ thống quản lý dữ liệu khách hàng (CRM) để khi một khách hàng mới được thêm vào, hệ thống tự động gửi thông tin khách hàng này qua webhook đến hệ thống tiếp thị qua email để bắt đầu một chiến dịch tiếp cận.


**Lưu ý:** Mỗi bot Telegram chỉ có thể có một webhook endpoint được cấu hình tại một thời điểm. Nếu bạn muốn thay đổi webhook để gửi dữ liệu tới một URL API khác, bạn sẽ phải cập nhật cấu hình webhook với Telegram Bot API bằng cách gọi phương thức setWebhook với URL mới.

