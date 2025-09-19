---
title: "Create crawler for Chplay-gold layer"
date: "2025-09-11"
weight: 2
chapter: false
pre: " <b> 5.2  </b> "
---

#### Create crawler for gold layer

For quick and focused setup, everyone should create the main crawler for the gold layer, and do the same for the rest!

1. Access **AWS Glue** interface
   - Select **Crawlers**
   - Select **Create crawler**

![Create VPC](/images/5/1.png?featherlight=false&width=90pc)

2. Enter:
   - Name: `chplay-gold`
   - Description: `Data after processed`
   - Select **Next**

![Create VPC](/images/5/2.png?featherlight=false&width=90pc)

3. Select **Add a data source**
   - Select the correct S3 folder: `chplay-gold`
   - Select **Next**

![Create VPC](/images/5/3.png?featherlight=false&width=90pc)

4. Select appropriate IAM role
   - Select **Next**

![Create VPC](/images/5/4.png?featherlight=false&width=90pc)

5. From **AWS Glue** interface
   - Select **Databases**
   - Select **Create database**
   - Name: `chplay-gold`
   - Select **Create database**

![Create VPC](/images/5/5.png?featherlight=false&width=90pc)

6. In the set Output section
   - Select Target database: `chplay-gold`
   - Select **Next**

![Create VPC](/images/5/6.png?featherlight=false&width=90pc)

Note:

{{% notice note %}}
You can choose folder hierarchy using the prefix option
{{% /notice %}}

7. Review everything once more

![Create VPC](/images/5/7.png?featherlight=false&width=90pc)

8. Click **Run crawler**

![Create VPC](/images/5/8.png?featherlight=false&width=90pc)

⇒ At this point, AWS Glue Crawler has created a catalog for 2 tables: app_details and app_reviews