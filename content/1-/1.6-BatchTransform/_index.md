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

**Một inference cho một model:**
- model_fn
- input_fn
- predict_fn
- output_fn

##### Ứng dụng thực tế
- Gắn nhãn/suy luận cho kho dữ liệu lịch sử (ví dụ: đánh giá ứng dụng đã thu thập trên S3).
- Tạo đặc trưng nâng cao (feature enrichment) cho pipeline phân tích báo cáo.
- Phân loại, phát hiện chủ đề/cảm xúc, lọc nội dung quy mô lớn.
- Chạy lại suy luận theo đợt khi có phiên bản mô hình mới.

##### Các lưu ý 

Use batch transform when you need to do the following:

- Preprocess datasets to remove noise or bias that interferes with training or inference from your dataset.
- Get inferences from large datasets.
- Run inference when you don't need a persistent endpoint.
- Associate input records with inferences to help with the interpretation of results.

. Note that Batch Transform doesn't support CSV-formatted input that contains embedded newline characters. You can control the size of the mini-batches by using the [`BatchStrategy`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html#sagemaker-CreateTransformJob-request-BatchStrategy) and [`MaxPayloadInMB`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html#sagemaker-CreateTransformJob-request-MaxPayloadInMB) parameters. `MaxPayloadInMB` must not be greater than 100 MB. If you specify the optional [`MaxConcurrentTransforms`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html#sagemaker-CreateTransformJob-request-MaxConcurrentTransforms) parameter, then the value of `(MaxConcurrentTransforms * MaxPayloadInMB)` must also not exceed 100 MB.