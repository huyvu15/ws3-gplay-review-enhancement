---
title : "Sagemaker Batch Transform"
date :  "2025-09-11" 
weight : 6 
chapter : false
pre : " <b> 1.6 </b> "
---

#### Sagemaker Batch Transform 

##### Giới thiệu
SageMaker Batch Transform là dịch vụ suy luận hàng loạt (offline) dùng để chạy mô hình ML trên tập dữ liệu có sẵn, lưu kết quả trực tiếp về S3. Phù hợp cho các kịch bản không yêu cầu độ trễ thấp và cần xử lý khối lượng dữ liệu lớn theo lô.

##### Khái niệm
- Chạy inference theo lô thay vì theo yêu cầu thời gian thực.
- Đọc dữ liệu đầu vào từ S3 và ghi kết quả ra S3 dưới dạng file.
- Không cần triển khai Endpoint, chỉ chạy khi có job nên tối ưu chi phí cho xử lý định kỳ.

##### Ứng dụng thực tế
- Gắn nhãn/suy luận cho kho dữ liệu lịch sử (ví dụ: đánh giá ứng dụng đã thu thập trên S3).
- Tạo đặc trưng nâng cao (feature enrichment) cho pipeline phân tích báo cáo.
- Phân loại, phát hiện chủ đề/cảm xúc, lọc nội dung quy mô lớn.
- Chạy lại suy luận theo đợt khi có phiên bản mô hình mới.
