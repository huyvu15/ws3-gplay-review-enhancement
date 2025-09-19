---
title: "Enhanced data for app review reports on market"
date: "2025-09-11"
weight: 1
chapter: false
---

# Enhanced Data for Google Play App Review Reports

![](https://citgroup.vn/wp-content/uploads/2024/02/app-giao-do-an-1.png)

<!-- ![Create VPC](/images/teleBot.webp?featherlight=false&width=75pc&height=30pc) -->

#### Overview

In the increasingly competitive mobile app landscape, monitoring and analyzing user feedback on Google Play is a crucial factor that helps development teams improve product quality. However, raw review data is often fragmented and difficult to immediately leverage for reporting purposes.

To address this, we can build an automated pipeline:

- Collect review data daily.

- Process and enrich data (e.g., user sentiment analysis).

- Store and visualize on dashboards.

Through this approach, reports don't just stop at review counts or ratings, but also provide deeper insights into user satisfaction levels, emotional trends over time, and areas for improvement.

#### Services Used:

The deployment process can leverage multiple AWS services to ensure **automation, flexible scaling, and cost optimization**:

**1. AWS Lambda Function:**  
- Run crawler function to retrieve review data from Google Play.  
- Automatically scale based on request volume, no server management required.  

**2. Amazon S3:**  
- Store raw data after scraping from Google Play.  
- Used as input/output in subsequent processing steps.  

**3. Amazon SageMaker (Batch Transform):**  
- Process review data using sentiment analysis models.  
- Run batch inference, cost-effective for periodic workloads.  

**4. Amazon EventBridge:**  
- Schedule daily pipeline triggers.  
- Ensure ETL process runs automatically without manual intervention.  

**5. Amazon Athena / Amazon Redshift (as needed):**  
- Query and aggregate processed data.  
- Serve as data source for reports/dashboards.  

**6. Amazon QuickSight:**  
- Data visualization.  
- Build dashboards to track sentiment trends, review counts, average ratings...  

→ However, for simplicity and the most convenient demonstration, this lab will only implement some simple features that can be executed immediately. Readers can easily develop additional features based on their individual needs and characteristics.

#### The primary language for this workshop is Python 3.12

<!-- ![Create VPC](/images/schema.png?featherlight=false&width=90pc) -->
![Create VPC](/images/schema.png)

#### Content

1. [Introduction](1-/)
2. [Preparation Steps](2-/)
3. [Create model on Sagemaker](3-/) 
4. [Create lambda for data collection and model triggering](4-/)
5. [Crawler and data processing on Glue](5-/)
6. [Create reports on QuickSight and Athena queries](6/)
7. [Resource cleanup](7-/)