---
title: "Create model on Sagemaker"
date: "2025-09-11"
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

#### Create model on Sagemaker AI

1. Access Sagemaker AI
   - Select **Inference**
   - Select **Models**
   - Select **Create Model**

![Create VPC](/images/2/3.png?featherlight=false&width=90pc)

2. Fill in the model configurations
   - Model name `distilbert-sst2`
   - IAM role: `abcxyz` (create an IAM role with sufficient permissions)

![Create VPC](/images/2/4.png?featherlight=false&width=90pc)

3. Continue scrolling down and fill in

   - Location of inference code image
   ```
   763104351884.dkr.ecr.ap-southeast-1.amazonaws.com/huggingface-pytorch-inference:1.13.1-transformers4.26.0-cpu-py39-ubuntu20.04
   ```

   - Location of model artifacts
   ```
   s3://glutisify-datalake/models/distilbert-sst2/model.tar.gz
   ```

   - Environment variables in the model:

   | Key                          | Value                     |
   |------------------------------|---------------------------|
   | HF_TASK                      | `text-classification`     |
   | SAGEMAKER_PROGRAM            | `inference.py`            |
   | SAGEMAKER_SUBMIT_DIRECTORY   | `/opt/ml/model/code`      |
   | SAGEMAKER_CONTAINER_LOG_LEVEL| `20`                      |
   | SAGEMAKER_REGION             | `ap-southeast-1`          |

![Create VPC](/images/2/5.png?featherlight=false&width=90pc)

4. Scroll to the bottom
   - Leave the remaining configurations as default
   - Select **Create**

![Create VPC](/images/2/6.png?featherlight=false&width=90pc)