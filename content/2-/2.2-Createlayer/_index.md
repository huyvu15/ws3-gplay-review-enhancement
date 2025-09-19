---
title : "Add Layer google_play_scraper"
date :  "2025-09-11" 
weight : 3
chapter : false
pre : " <b> 2.3 </b> "
---

#### Add Layer google_play_scraper

There are many pre-built layers packaged and shared by other users on GitHub repositories. However, those are only very common layers, while most other libraries won't be available as such.

Here I will guide you on how to package layers collectively.

**A few things to note:**
- Not every package can be packaged as a layer, AWS only allows a maximum zip size of 50MB, and 250MB on S3
- For package creation, you can create locally and push to S3

**Current tasks needed:**
- Prepare a Linux server (could be your machine) or use Cloud Shell directly
- Have AWS CLI installed
- Execute the following commands sequentially:

1. Create directory structure
```bash
mkdir google_play_scraper_layer
cd google_play_scraper_layer
mkdir -p python
```

2. Install Python library

```bash
pip install google_play_scraper -t python/
```

3. Package as zip

```bash
zip -r9 google_play_scraper_layer.zip python
```

4. Upload file to S3

```bash
aws s3 cp dist/google_play_scraper-0.1.0-py3-none-any.whl s3://glutisify/package/
```
#### Create layer on the interface

1. In the **AWS Management Console**

   - Select **Lambda**
   - Select **Layer**
   - Select **Create layer**

![Create VPC](/images/2/1.png?featherlight=false&width=90pc)


2. Continue to select

- At name field, enter ```google_play_scraper```
- At description field, enter ``` google_play_scraper package```
- Choose upload from S3
- At Amazon S3 link URL field, enter ```s3://glutisify-datalake/package/google_play_scraper_layer.zip```
- At architectures, select ```arm64, x86_64```
- Select ```Python 3.12```
- Select **Create**

![Create VPC](/images/2/2.png?featherlight=false&width=90pc)


#### Reference
[pip install google_play_scraper](https://pypi.org/project/google-play-scraper/)