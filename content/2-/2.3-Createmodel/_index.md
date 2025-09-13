---
title : "Tạo model distilbert-sst2 và đẩy lên s3"
date :  "2025-09-11" 
weight : 3
chapter : false
pre : " <b> 2.3 </b> "
---

#### Tải model về máy

1. Tạo file main.py:

```bash
vi main.py
```

Thêm nội dung file:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_id = "distilbert-base-uncased-finetuned-sst-2-english"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

tokenizer.save_pretrained("./distilbert-sst2")
model.save_pretrained("./distilbert-sst2")
```

Run code:
```bash
uv run main.py
```

1. Truy cập vào phần model
- Tạo 1 folder mới chưa inference

```bash
mkdir code
cd code
vi inference.py
```

Thêm nội dung:
```python
import json
import os
from transformers import pipeline
from langdetect import detect, LangDetectException

def model_fn(model_dir):
    """
    Hàm này được SageMaker gọi để tải model.
    Linh hoạt với cấu trúc thư mục của model.
    """
    candidate_subdir = os.path.join(model_dir, "model")
    model_path = candidate_subdir if os.path.isdir(candidate_subdir) else model_dir
    
    sentiment_pipeline = pipeline(
        "text-classification",
        model=model_path,
        tokenizer=model_path,
        device=-1, 
        top_k=1
    )
    return sentiment_pipeline

def input_fn(request_body, request_content_type):
    """
    Hàm này xử lý một dòng JSON duy nhất, phù hợp với BatchStrategy=SINGLE_RECORD.
    """
    if request_content_type == 'application/jsonlines':
        if isinstance(request_body, bytes):
            request_body = request_body.decode('utf-8')
        return json.loads(request_body)
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model):
    """
    Hàm này thực hiện dự đoán trên một record duy nhất.
    Quan trọng: Nó sẽ phát hiện ngôn ngữ trước khi dự đoán.
    """
    review_text = input_data.get('content', '').strip()
    
    if not review_text:
        input_data['sentiment_prediction'] = {'label': 'NO_CONTENT'}
        return input_data

    try:
        lang = detect(review_text)
        
        if lang == 'en':
            sentiment_result = model(review_text)[0] 
            input_data['sentiment_prediction'] = sentiment_result
        else:
            input_data['sentiment_prediction'] = {'label': 'NON_ENGLISH', 'language_detected': lang}

    except LangDetectException:
        input_data['sentiment_prediction'] = {'label': 'LANG_DETECT_ERROR'}
        
    return input_data

def output_fn(prediction, accept):
    """
    Hàm này định dạng kết quả đầu ra cho một record.
    """
    if accept == "application/jsonlines":
        return json.dumps(prediction, ensure_ascii=False) + '\n'
    
    raise ValueError(f"Unsupported accept type: {accept}")
```

3. Nén lại tành file model..tar
```bash
tar -czf model.tar.gz distilbert-sst2/
```

4. Đẩy lên s3
```bash
aws s3 cp distilbert-sst2-fixed.tar.gz s3://glutisify-datalake/models/distilbert-sst2-fixed/
```



{{% notice tip %}}
Các file code trên chỉ hiệu quả khi bạn cài xong môi trường, ở đây mình dùng uv do uv nhanh gấp 10 lần pip
{{% /notice %}}




