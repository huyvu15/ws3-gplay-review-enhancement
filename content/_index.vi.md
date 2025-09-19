---
title : "Tăng cường dữ liệu cho báo cáo đánh giá app trên market"
date :  "2025-09-11" 
weight : 1 
chapter : false
---

# Tăng cường dữ liệu cho báo cáo đánh giá app trên Google Play

![](https://citgroup.vn/wp-content/uploads/2024/02/app-giao-do-an-1.png)

<!-- ![Create VPC](/images/teleBot.webp?featherlight=false&width=75pc&height=30pc) -->


#### Tổng quan

Trong bối cảnh ứng dụng di động ngày càng cạnh tranh, việc theo dõi và phân tích phản hồi của người dùng trên Google Play là yếu tố quan trọng giúp đội ngũ phát triển cải thiện chất lượng sản phẩm. Tuy nhiên, dữ liệu đánh giá thô thường rời rạc và khó khai thác ngay cho mục đích báo cáo.

Để khắc phục điều này, ta có thể xây dựng một pipeline tự động hóa:

- Thu thập dữ liệu đánh giá hằng ngày.

- Xử lý và làm giàu dữ liệu (ví dụ phân tích cảm xúc người dùng).

- Lưu trữ và trực quan hóa trên dashboard.

Nhờ cách tiếp cận này, báo cáo không chỉ dừng ở số lượng review hay rating, mà còn cung cấp cái nhìn sâu hơn về mức độ hài lòng của người dùng, xu hướng cảm xúc theo thời gian, và các điểm cần cải thiện.


#### Các Service sử dụng:

Quy trình triển khai có thể tận dụng nhiều dịch vụ AWS để đảm bảo **tự động, mở rộng linh hoạt và tối ưu chi phí**:

**1. AWS Lambda Function:**  
- Chạy function crawler để lấy dữ liệu review từ Google Play.  
- Tự động scale theo số lượng request, không cần quản lý server.  

**2. Amazon S3:**  
- Lưu trữ dữ liệu thô (raw data) sau khi cào từ Google Play.  
- Dùng làm input/output trong các bước xử lý tiếp theo.  

**3. Amazon SageMaker (Batch Transform):**  
- Xử lý dữ liệu review bằng mô hình sentiment analysis.  
- Chạy inference theo batch, tiết kiệm chi phí cho workload định kỳ.  

**4. Amazon EventBridge:**  
- Đặt lịch trigger pipeline hằng ngày.  
- Đảm bảo quy trình ETL diễn ra tự động mà không cần can thiệp thủ công.  

**5. Amazon Athena / Amazon Redshift (tùy nhu cầu):**  
- Truy vấn và tổng hợp dữ liệu đã xử lý.  
- Làm nguồn dữ liệu cho báo cáo/dashboard.  

**6. Amazon QuickSight:**  
- Trực quan hóa dữ liệu.  
- Xây dựng dashboard theo dõi xu hướng sentiment, số lượng review, rating trung bình…  



→ Tuy nhiên để đơn giản và demo một cách thuận tiện nhất có thể bài lab chỉ thực hiện một số những tính năng đơn giản và có thể thực hiện được ngay. Độc giả có thể dễ dàng phát triển thêm các tinh năng khác dựa theo từng nhu cầu và đặc điểm của bản thân. 

#### Ngôn ngữ chính để phục vụ workshop này là python 3.12

<!-- ![Create VPC](/images/schema.png?featherlight=false&width=90pc) -->
![Create VPC](/images/schema.png)


#### Nội dung

1. [Giới thiệu](1-/)
2. [Các bước chuẩn bị](2-/)
3. [Tạo model trên Sagemaker](3-/) 
5. [Tạo lambda lấy dữ liệu và trigger model](4-/)
6. [Crawler và xử lý dữ liệu trên Glue](5-/)
7. [Tạo báo cáo trên QuickSight và truy vấn Athena](6/)
8. [Dọn dẹp tài nguyên](7-/)    