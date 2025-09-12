---
title : "Giới thiệu"
date :  "2025-09-11" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

# Tăng cường dữ liệu cho báo cáo đánh giá app trên Google Play

#### Tổng quan

Dạo gần đây với sự nổi lên của các chatbot thông minh như OpenAI, Claude, Bing,... với những tính năng vô cùng mạnh mẽ. Vì vậy mình cũng muốn tạo ra một con chatbot đơn giản của riêng bản thân. Trong workshop này, bạn sẽ học cách thiết kế và lập trình một chatbot trên Telegram, giúp bạn tiện lợi theo dõi và quản lý chi tiêu cá nhân mà không cần đăng nhập.

Telegram là một ứng dụng nhắn tin phổ biến, mạnh mẽ và là lựa chọn lý tưởng để phát triển chatbot quản lý chi tiêu.


#### Các Service sử dụng:

**1. AWS Lambda Function:** là dịch vụ điện toán phi máy chủ (serverless) do Amazon cung cấp, cho phép bạn chạy các đoạn mã mà không cần quản lý máy chủ. Với Lambda, bạn chỉ cần tải lên mã của mình và AWS sẽ lo phần còn lại, bao gồm việc cung cấp tài nguyên máy tính và tự động scale mã của bạn dựa trên nhu cầu.


**2. Amazon S3:** kho lưu trữ dung lượng lớn, chi phí thấp và an toàn, phù hợp với nhiều nhu cầu lưu trữ dữ liệu.


**3. Amazon DynamoDB:** Dịch vụ cơ sở dữ liệu NoSQL hiệu suất cao, tự động điều chỉnh quy mô theo nhu cầu.

**4. API Gateway:** Dịch vụ quản lý API giúp tạo, xuất bản, duy trì và bảo mật các API ở bất kỳ quy mô nào.

Workshop sẽ tập trung vào các tính năng đơn giản, dễ thực hiện. Người dùng có thể phát triển thêm các tính năng khác dựa trên nhu cầu cá nhân. 

Ngôn ngữ chính để phục vụ workshop này là python 3.10


#### Ý tưởng: 

Viết một API Gateway để kết nối với telegram và kích hoạt thông qua webhook. API đó được gắn với một lambda function có nhiệm vụ đọc và ghi dữ liệu, truy vấn kết quả truy vấn đến dynamodb. Tùy vào mục đích sử dụng ta có thể sáng tạo công dụng của chatbot theo ý muốn:

Một số những thống kê có thể kể đến:

- Tổng số tiền chi tiêu trong tháng.

- Tổng tiền ăn.

- Tổng số tiền đổ xăng.

- Các chi tiêu gần nhất.


#### Bạn có thể làm gì với dữ liệu từ ChatBot

Ngoài việc để theo dõi thu chi cá nhân hiện tại. Bạn có thể sử dụng dữ liệu này cho các mô hình machine learning đơn giản để dự báo chi tiêu cũng như đưa ra cảnh báo nếu như thu chi bị biến động quá nhiều. Hoặc đưa gia các gợi ý thích hợp và chi tiêu thích hợp cho các tháng tiếp theo.


#### Nội dung

1. [Giới thiệu](1-/)
2. [Tạo chatbot trên Telegram](2-/)
3. [Các bước chuẩn bị](3-/) 
4. [Tạo API Gateway](4-/)
5. [Tạo bảng trong DynamoDB](5-/)
6. [Sử dụng Chatbot](6/)
7. [Dọn dẹp tài nguyên](7-/)

Bây giờ chúng ta sẽ cùng nhau đi qua các khái niệm cơ bản nhất của Lambda Function.
