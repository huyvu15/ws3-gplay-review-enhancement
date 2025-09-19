---
title : "Tạo job ETL bằng Glue job"
date :  "2025-09-11" 
weight : 1
chapter : false
pre : " <b> 5.1  </b> "
---


#### Tạo job ETL bằng Glue job

1. Truy cập giao diện **AWS Glue**
- Chọn **ETL jobs**
- Chọn **Visual ETL**
- Chọn **Script editor**

![Create VPC](/images/5/9.png?featherlight=false&width=90pc)

2. Với Engine: **Spark**
- Chọn **Create script**
![Create VPC](/images/5/10.png?featherlight=false&width=90pc)

3. Tại giao diện ETL job:
- Rename job thành: ```Chplay-transform-to-gold-layer```
- Copy Scrip sau:
 

```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, udf, lower, when, lit
from pyspark.sql.types import StringType, DoubleType

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

dyf_reviews = glueContext.create_dynamic_frame.from_options(
    format_options={"multiLine": "false"},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://glutisify-datalake/chplay-silver/app_reviews/"],
        "recurse": True
    },
    transformation_ctx="Reviews_node"
)
df_reviews = dyf_reviews.toDF()

def extract_label(predictions):
    return predictions[0]["label"]

def extract_score(predictions):
    return float(predictions[0]["score"])

extract_label_udf = udf(extract_label, StringType())
extract_score_udf = udf(extract_score, DoubleType())

performance_keywords = ['slow', 'lag', 'crash', 'bug', 'error', 'load']
performance_regex = "|".join([f"\\b{kw}\\b" for kw in performance_keywords])

df_reviews_parsed = (
    df_reviews.withColumn("sentiment_label", extract_label_udf(col("sentiment_prediction")))
              .withColumn("sentiment_score", extract_score_udf(col("sentiment_prediction")))
              .drop("sentiment_prediction")
              .drop("userImage")
              .withColumn(
                  "mentions_ads",
                  when(lower(col("content")).rlike("ads?|advertis(e|ing)"), True).otherwise(False)
              )
              .withColumn(
                  "mentions_performance_issue",
                  when(lower(col("content")).rlike(performance_regex), True).otherwise(False)
              )
)

dyf_details = glueContext.create_dynamic_frame.from_options(
    format_options={"multiLine": "false"},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://glutisify-datalake/chplay/app_details/"],
        "recurse": True
    },
    transformation_ctx="Details_node"
)
df_details = dyf_details.toDF()

from pyspark.sql.types import StringType

df_details_fixed = df_details.select(
    *[
        col(c).cast(StringType()) if dict(df_details.dtypes)[c] == "void" else col(c)
        for c in df_details.columns
    ]
)

df_details_parsed = (
    df_details_fixed
        .withColumn("categories_name", col("categories")[0]["name"])
        .withColumn("categories_id", col("categories")[0]["id"])
        .drop("categories", "descriptionHTML", "icon", "headerImage", "screenshots", "histogram")
)

(
    df_reviews_parsed
    .write
    .mode("overwrite")
    .partitionBy("crawled_at")
    .parquet("s3://glutisify-datalake/chplay-gold/app_reviews/")
)

(
    df_details_parsed
    .write
    .mode("overwrite")
    .partitionBy("crawled_at")
    .parquet("s3://glutisify-datalake/chplay-gold/app_details/")
)

job.commit()
```

- Chọn **Save**

![Create VPC](/images/5/11.png?featherlight=false&width=90pc)

4. Chuyển sang tab **Job details**
- Chọn IAM role phù hợp


![Create VPC](/images/5/12.png?featherlight=false&width=90pc)

5. Run Job
- Chọn **Run**

![Create VPC](/images/5/13.png?featherlight=false&width=90pc)


6. Job run thành công

![Create VPC](/images/5/15.png?featherlight=false&width=90pc)


7. Check dữ liệu trên gold layer s3:

![Create VPC](/images/5/14.png?featherlight=false&width=90pc)

=> Dữ liệu được đổ sang và tối ưu lưu trữ ở định dạng Parquet