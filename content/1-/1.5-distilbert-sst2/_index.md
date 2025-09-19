---
title : "Mô hình distilbert-sst2"
date :  "2025-09-11" 
weight : 5
chapter : false
pre : " <b> 1.5 </b> "
---

#### Mô hình distilbert-sst2

![](https://www.mdpi.com/electronics/electronics-09-00483/article_deploy/html/images/electronics-09-00483-g001.png)

##### Giới thiệu
distilBERT-SST2 là mô hình DistilBERT được tinh chỉnh trên tập dữ liệu SST-2 để phân tích cảm xúc nhị phân (tích cực/tiêu cực) ở cấp câu. Mô hình nhỏ gọn, suy luận nhanh, độ chính xác tốt cho các bài toán sentiment phổ biến.

##### Khái niệm
- DistilBERT là phiên bản rút gọn của BERT qua kỹ thuật knowledge distillation: ít tham số hơn (~40%), suy luận nhanh hơn (đến ~60%) nhưng giữ phần lớn hiệu năng của BERT.
- SST-2 (Stanford Sentiment Treebank v2) gán nhãn cảm xúc nhị phân cho câu; đầu ra mô hình là xác suất/nhãn Positive hoặc Negative.
- Kết quả thường lấy theo Softmax trên hai lớp; có thể tùy ngưỡng cho các mục tiêu kinh doanh khác nhau.

##### Phân loại văn bản thành tích cực tiêu cực

Sở dĩ dùng model trên do dữ liệu lấy về có cột content chứa đánh giá của người dùng

##### Cách triển khai nhanh

**Hugging Face Transformers:**
```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
print(classifier("This product is awesome!"))
```

Output: ```{'label': 'POSITIVE', 'score': 0.999}```

Triển khai dễ dàng trong Flask/FastAPI để làm API phục vụ real-time.


##### Ứng dụng thực tế
- Phân tích cảm xúc đánh giá ứng dụng, phản hồi khách hàng, bài đăng mạng xã hội.
- Cảnh báo sớm và ưu tiên xử lý phản hồi tiêu cực trong quy trình hỗ trợ.
- Theo dõi xu hướng cảm xúc theo thời gian cho báo cáo thương hiệu/sản phẩm.
- Là bước tiền xử lý cho các pipeline nâng cao: phân loại chủ đề, định tuyến ticket, tóm tắt.
