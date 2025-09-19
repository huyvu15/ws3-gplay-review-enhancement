---
title : "Introduction"
date :  "2025-09-11" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

#### Overview

In mobile application development, understanding user feedback is crucial to improving product quality, enhancing user experience, and retaining customers. On Google Play, apps receive countless reviews and ratings every day. However, this data often exists in a scattered form, making it difficult to analyze directly by just looking at raw statistics.

An effective review report should go beyond simply aggregating the number of reviews or calculating the average rating. It needs to dig deeper into questions such as:

- Are users feeling positive or negative about the app?
- What percentage of users report issues related to performance, ads, etc.?
- How do sentiment trends change over time?

To answer these questions, we need an automated solution for collecting, processing, and visualizing the data.

#### Services Used

The implementation process can leverage multiple AWS services to ensure **automation, scalability, and cost optimization**:

**1. AWS Lambda Function:**  
- Runs a crawler function to fetch review data from Google Play.  
- Automatically scales with requests, with no server management required.  

**2. Amazon S3:**  
- Stores raw data after crawling from Google Play.  
- Serves as input/output storage for subsequent processing steps.  

**3. Amazon SageMaker (Batch Transform):**  
- Processes review data with a sentiment analysis model.  
- Runs inference in batches, reducing costs for periodic workloads.  

**4. Amazon EventBridge:**  
- Schedules daily pipeline triggers.  
- Ensures the ETL process runs automatically without manual intervention.  

**5. Amazon Athena / Amazon Redshift (depending on use case):**  
- Queries and aggregates processed data.  
- Provides data sources for reports and dashboards.  

**6. Amazon QuickSight:**  
- Visualizes the data.  
- Builds dashboards to track sentiment trends, review counts, average ratings, etc.  

#### Concept

The idea comes from a real-world need: every day, an app receives hundreds to thousands of new reviews on Google Play. Looking only at the average rating is not enough to capture the full user experience. Therefore, we need a mechanism that can:

- **Automate review crawling:** No manual work required, ensuring data is always up-to-date.  
- **Analyze sentiment with AI/ML:** Transform user text into structured data (positive, negative, neutral sentiment).  
- **Integrate storage – processing – visualization:** Turn raw files into meaningful business insights.  
- **Run on schedule:** Triggered periodically (e.g., daily) to ensure reports are always fresh.  

The solution can be visualized as a complete data pipeline:

- **Ingestion:** Crawl reviews from Google Play.  
- **Storage:** Store raw data in S3.  
- **Processing:** Clean and analyze sentiment with SageMaker.  
- **Analytics:** Query using Athena or Redshift.  
- **Visualization:** Dashboard with QuickSight.  
- **Automation:** EventBridge + Step Functions ensure the pipeline runs reliably and consistently.  

#### Contents

1. [Introduction](1-/)  
2. [Preparation Steps](2-/)  
3. [Building a Model on SageMaker](3-/)  
4. [Creating Lambda to Fetch Data and Trigger the Model](4-/)  
5. [Crawler and Data Processing on Glue](5-/)  
6. [Reporting on QuickSight and Querying with Athena](6-/)  
7. [Resource Cleanup](7-/)  

Now, let’s walk through the fundamental concepts of crawling data.
