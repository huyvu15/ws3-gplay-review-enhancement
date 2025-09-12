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
---
title : "Mô hình distilbert-sst2"
date :  "2025-09-11" 
weight : 6
chapter : false
pre : " <b> 1.6 </b> "
---

#### Mô hình distilbert-sst2

##### Giới thiệu
distilBERT-SST2 là mô hình DistilBERT được tinh chỉnh trên tập dữ liệu SST-2 để phân tích cảm xúc nhị phân (tích cực/tiêu cực) ở cấp câu. Mô hình nhỏ gọn, suy luận nhanh, độ chính xác tốt cho các bài toán sentiment phổ biến.

##### Khái niệm
- DistilBERT là phiên bản rút gọn của BERT qua kỹ thuật knowledge distillation: ít tham số hơn (~40%), suy luận nhanh hơn (đến ~60%) nhưng giữ phần lớn hiệu năng của BERT.
- SST-2 (Stanford Sentiment Treebank v2) gán nhãn cảm xúc nhị phân cho câu; đầu ra mô hình là xác suất/nhãn Positive hoặc Negative.
- Kết quả thường lấy theo Softmax trên hai lớp; có thể tùy ngưỡng cho các mục tiêu kinh doanh khác nhau.

##### Ứng dụng thực tế
- Phân tích cảm xúc đánh giá ứng dụng, phản hồi khách hàng, bài đăng mạng xã hội.
- Cảnh báo sớm và ưu tiên xử lý phản hồi tiêu cực trong quy trình hỗ trợ.
- Theo dõi xu hướng cảm xúc theo thời gian cho báo cáo thương hiệu/sản phẩm.
- Là bước tiền xử lý cho các pipeline nâng cao: phân loại chủ đề, định tuyến ticket, tóm tắt.
