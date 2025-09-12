---
title : "AWS Data Pipeline: Phân tích đánh giá ứng dụng Google Play"
date :  "2025-01-15" 
weight : 1 
chapter : false
---

# 🚀 AWS Data Pipeline: Phân tích đánh giá ứng dụng Google Play

![AWS Data Pipeline Logo](/images/logo.svg)

## 🎯 Mục tiêu Workshop

Xây dựng pipeline tự động phân tích sentiment từ đánh giá ứng dụng Google Play sử dụng AWS services


#### Tổng quan

Trong bối cảnh ứng dụng di động ngày càng cạnh tranh, việc theo dõi và phân tích phản hồi của người dùng trên Google Play là yếu tố quan trọng giúp đội ngũ phát triển cải thiện chất lượng sản phẩm. Tuy nhiên, dữ liệu đánh giá thô (reviews) thường rời rạc và khó khai thác ngay cho mục đích báo cáo.

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

#### 🛠️ Yêu cầu tiên quyết

**📚 Kiến thức cần có:**
- AWS cơ bản (S3, Lambda, SageMaker)
- Python 3.12+
- JSON và API

**⏱️ Thời gian:**
- Tổng thời gian: 3-4 giờ
- Mỗi phần: 30-45 phút
- Có thể làm theo nhóm

**💰 Chi phí ước tính:**
- Free tier: $0-5
- Production: $10-20/tháng
- Có hướng dẫn tối ưu

#### 🎨 Kiến trúc tổng quan

![AWS Data Pipeline Architecture](/images/schema.png)


#### 📋 Nội dung Workshop

1. **[📖 Giới thiệu](1-/)** - Tổng quan về pipeline và các AWS services
2. **[⚙️ Chuẩn bị](2-/)** - Setup AWS account và môi trường  
3. **[🕷️ Crawler](3-/)** - Xây dựng crawler lấy dữ liệu Google Play
4. **[🤖 ML Processing](4-/)** - Tạo Batch Transform job với SageMaker
5. **[📊 Data Warehouse](5-/)** - Tạo và đẩy dữ liệu lên Athena
6. **[📈 Dashboard](6/)** - Dựng dashboard trên QuickSight
7. **[🧹 Cleanup](7-/)** - Dọn dẹp tài nguyên AWS

#### 🎯 Kết quả mong đợi

Sau khi hoàn thành workshop, bạn sẽ có:

- ✅ **Pipeline tự động** thu thập và xử lý dữ liệu review
- ✅ **Dashboard trực quan** hiển thị sentiment analysis  
- ✅ **Kiến thức thực tế** về AWS services
- ✅ **Code template** có thể tái sử dụng cho dự án khác

#### 💡 Lưu ý quan trọng

- Tuân thủ Terms of Service của Google Play Store
- Sử dụng rate limiting để tránh bị block
- Monitor chi phí AWS thường xuyên
- Backup dữ liệu quan trọng