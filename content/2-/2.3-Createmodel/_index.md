---
title : "Create distilbert-sst2 model and upload to s3"
date :  "2025-09-11" 
weight : 4
chapter : false
pre : " <b> 2.4 </b> "
---

#### Download model to local machine

1. Create main.py file:

```bash
vi main.py
```

Add file content:

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

1. Access the model section
- Create a new folder for inference

```bash
mkdir code
cd code
vi inference.py
```

Add content:
```python
import json
import os
from transformers import pipeline

def model_fn(model_dir):
    """
    This function is called by SageMaker to load the model.
    Flexible with model directory structure.
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
    This function processes a single JSON line, suitable for BatchStrategy=SINGLE_RECORD.
    """
    if request_content_type == 'application/jsonlines':
        if isinstance(request_body, bytes):
            request_body = request_body.decode('utf-8')
        return json.loads(request_body)
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model):
    """
    This function performs prediction on a single record.
    Important: It will detect language before prediction.
    """
    review_text = input_data.get('content', '').strip()
    
    sentiment_result = model(review_text)[0] 
    input_data['sentiment_prediction'] = sentiment_result
        
    return input_data

def output_fn(prediction, accept):
    """
    This function formats the output result for one record.
    """
    if accept == "application/jsonlines":
        return json.dumps(prediction, ensure_ascii=False) + '\n'
    
    raise ValueError(f"Unsupported accept type: {accept}")
```

3. Compress into model.tar file
```bash
tar -czf model.tar.gz distilbert-sst2/
```
- Should use this code for compression:

```python
import os
import shutil
import tarfile
import json
import textwrap

def fix_model_package():
    temp_dir = "temp_model_fixed"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    try:
        model_dest = os.path.join(temp_dir, "model")
        shutil.copytree("distilbert-sst2", model_dest)
        
        code_dest = os.path.join(temp_dir, "code")
        os.makedirs(code_dest)
        
        shutil.copy("distilbert-sst2/code/inference.py", code_dest)
        
        requirements_content = textwrap.dedent("""
            transformers
            torch
            sagemaker-inference
        """).strip()

        with open(os.path.join(code_dest, "requirements.txt"), "w") as f:
            f.write(requirements_content)

        tar_filename = "model.tar.gz"
        with tarfile.open(tar_filename, "w:gz") as tar:
            tar.add(temp_dir, arcname=".")

        shutil.rmtree(temp_dir)
        
    except Exception as e:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        raise
if __name__ == "__main__":
    fix_model_package()
```

1. Upload to S3
```bash
aws s3 cp model.tar.gz s3://glutisify-datalake/models/distilbert-sst2-fixed/
```

{{% notice tip %}}
The code files above are only effective when you have completed the environment setup. Here I use uv because uv is 10 times faster than pip
{{% /notice %}}