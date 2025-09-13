---
title : "Add Layer google_play_scraper"
date :  "2025-09-11" 
weight : 2 
chapter : false
pre : " <b> 2.2 </b> "
---

#### Add Layer google_play_scraper

Có rất nhiều layer có sẵn được các người dùng khác đóng gói và chia sẻ trên các repo github. Tuy nhiên đó chỉ là các layer rất là phổ biến còn đa số các thư viện còn lại sẽ không được như vậy.

Tại đây mình sẽ hướng dẫn bạn đóng gói chung cho các layer

**Một vài cái cần phải lưu ý:**
- Không phải package nào cũng đóng gói được thành layer, AWS chỉ cho phép kích thước zip tối đa là 50MB, và 250MB trên s3
- Việc tạo package bạn có thể tạo ở local và đấy ngược lên s3

**Việc hiện tại cần làm:**
- Chuẩn bị một server linux (có thể là máy bạn) hoặc dùng trực tiếp cloud shell
- Đã cài aws cli
- Thực hiện lần lượt các câu lệnh sau:

1. Tạo cấu trúc thư mục
```bash
mkdir google_play_scraper_layer
cd google_play_scraper_layer
mkdir -p python
```

2. Cài thư viện Python

```bash
pip install google_play_scraper -t python/
```

3. Đóng gói zip

```bash
zip -r9 google_play_scraper_layer.zip python
```

4. Upload file lên s3

```bash
aws s3 cp dist/google_play_scraper-0.1.0-py3-none-any.whl s3://glutisify/package/
```
#### Tạo layer trên giao diện

1. Trong giao diện **AWS Management Console**

   - Chọn **Lambda**
   - Chọn **Layer**
   - Chọn **Create layer**

![Create VPC](/images/2/1.png?featherlight=false&width=90pc)


2. Tiếp tục chọn

- Tại name điền ```google_play_scraper```
- Tại description điền ``` google_play_scraper package```
- Chọn upload từ s3
- Tại Amazon S3 link URL điền ```s3://glutisify-datalake/package/google_play_scraper_layer.zip```
- Tại architectures chọn ```arm64, x86_64```
- Chọn ```Python 3.12```
- Chọn **Create**

![Create VPC](/images/2/2.png?featherlight=false&width=90pc)

=> Đây là cách 1 layer được ra đời :>>

#### Tham khảo
[pip install google_play_scraper](https://pypi.org/project/google-play-scraper/)
