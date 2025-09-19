---
title : "Giới thiệu"
date :  "2025-09-11" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

# 

#### Tổng quan

Trong quá trình phát triển ứng dụng di động, việc hiểu rõ phản hồi của người dùng là yếu tố sống còn để cải thiện chất lượng sản phẩm, nâng cao trải nghiệm và giữ chân khách hàng. Trên Google Play, mỗi ngày ứng dụng nhận được hàng loạt đánh giá và xếp hạng. Tuy nhiên, dữ liệu này thường tồn tại dưới dạng rời rạc, khó phân tích trực tiếp nếu chỉ nhìn vào bảng thống kê đơn thuần.

Một báo cáo đánh giá hiệu quả không chỉ dừng lại ở việc tổng hợp số lượng review hay tính trung bình rating, mà cần khai thác sâu hơn:

- Người dùng đang cảm thấy tích cực hay tiêu cực về ứng dụng?

- Tỷ lệ báo cáo của người dùng về hiệu năng, quảng cáo,..?

- Xu hướng cảm xúc thay đổi ra sao theo thời gian?

Để trả lời những câu hỏi này, chúng ta cần một giải pháp tự động hóa thu thập, xử lý và trực quan hóa dữ liệu.

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

#### Ý tưởng: 

Ý tưởng xuất phát từ nhu cầu thực tế: hằng ngày ứng dụng có hàng trăm đến hàng nghìn review mới trên Google Play. Nếu chỉ nhìn vào bảng rating trung bình thì chưa đủ để phản ánh toàn diện trải nghiệm của người dùng. Do đó, cần một cơ chế:

- Tự động cào dữ liệu review: Không cần thao tác thủ công, đảm bảo dữ liệu luôn cập nhật.

- Phân tích cảm xúc bằng AI/ML: Biến các đoạn text của người dùng thành dữ liệu có cấu trúc (sentiment: tích cực, tiêu cực, trung lập).

- Tích hợp lưu trữ – xử lý – trực quan hóa: Giúp dữ liệu không chỉ nằm trên file mà còn trở thành thông tin có giá trị kinh doanh.

- Hoạt động định kỳ: Trigger theo lịch (ví dụ: mỗi ngày), đảm bảo báo cáo luôn mới nhất.

Mô hình giải quyết bài toán này có thể hình dung như một data pipeline hoàn chỉnh:

- Ingestion (Thu thập): Crawl review từ Google Play.

- Storage (Lưu trữ): Đưa dữ liệu raw vào S3.

- Processing (Xử lý): Làm sạch, phân tích sentiment qua SageMaker.

- Analytics (Phân tích): Query bằng Athena hoặc Redshift.

- Visualization (Trực quan hóa): Dashboard bằng QuickSight.

Automation (Tự động hóa): EventBridge + Step Functions đảm bảo pipeline chạy đều đặn và bền vững.


#### Nội dung

1. [Giới thiệu](1-/)
2. [Các bước chuẩn bị](2-/)
3. [Tạo model trên Sagemaker](3-/) 
5. [Tạo lambda lấy dữ liệu và trigger model](4-/)
6. [Crawler và xử lý dữ liệu trên Glue](5-/)
7. [Tạo báo cáo trên QuickSight và truy vấn Athena](6/)
8. [Dọn dẹp tài nguyên](7-/)    

Bây giờ chúng ta sẽ cùng nhau đi qua các khái niệm cơ bản nhất của việc crawl data
