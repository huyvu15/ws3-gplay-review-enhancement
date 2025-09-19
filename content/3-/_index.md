---
title : "Tạo model trên Sagemaker"
date :  "2025-09-11" 
weight : 3 
chapter : false
pre : " <b> 3. </b> "
---

#### Tạo model trên sagemaker AI

1. Truy cập Sagemaker AI
- Chọn **Inference**
- Chọn **Models**
- Chọn **Create Model**


![Create VPC](/images/2/3.png?featherlight=false&width=90pc)

2. Điền các cấu hình cho model
- Model name ```distilbert-sst2```
- IAM role: ```abcxyz``` (tạo 1 IAM role có đủ quyền)

![Create VPC](/images/2/4.png?featherlight=false&width=90pc)


3. Tiếp tục kéo xuống và điền

- Location of inference code image
```
763104351884.dkr.ecr.ap-southeast-1.amazonaws.com/huggingface-pytorch-inference:1.13.1-transformers4.26.0-cpu-py39-ubuntu20.04
```

- Location of model artifacts
```
s3://glutisify-datalake/models/distilbert-sst2/model.tar.gz
```

- Các biến môi trường trong model:

| Key                          | Value                     |
|------------------------------|---------------------------|
| HF_TASK                      | ```text-classification```       |
| SAGEMAKER_PROGRAM            | ```inference.py```            |
| SAGEMAKER_SUBMIT_DIRECTORY   | ```/opt/ml/model/code ```       |
| SAGEMAKER_CONTAINER_LOG_LEVEL| ```20```                      |
| SAGEMAKER_REGION             | ```ap-southeast-1   ```         |


![Create VPC](/images/2/5.png?featherlight=false&width=90pc)

4. Kéo xuống cuối
- Để các config còn lại mặc định
- Chọn **Create**
![Create VPC](/images/2/6.png?featherlight=false&width=90pc)