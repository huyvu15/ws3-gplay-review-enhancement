---
title : "Clean Up Resources"
date :  "2025-09-11" 
weight : 7
chapter : false
pre : " <b> 7. </b> "
---

#### Clean Up Resources

In this lab, we have used services such as S3, Lambda Function, QuickSight, Glue Job, and Sagemaker AI. These services are relatively cheap and even free for 12 months under the free-tier account, so it is not strictly necessary to delete them.  

However, if you still want to delete them, here are the steps:

##### Delete S3 Bucket
Go to S3, select the bucket **glutisify-datalake**, then choose **Empty**. After that, click **Delete** and follow the on-screen instructions to remove it.

##### Delete Lambda Functions
Go to the Lambda function console, select the functions **run-sentiment-app-review-batch-transform**, **crawl-app-details-maket-chplay**, **crawl-review-maker-chplay**, then choose **Actions** → **Delete** to remove them.

##### Delete Model on Sagemaker AI
Access the Sagemaker AI console, select the model you created, and delete it to avoid additional costs.

##### Delete Schedule on EventBridge
Access the EventBridge console and remove the schedules you created.

##### Delete QuickSight Account

1. Go to the QuickSight console, then navigate to **Account settings**  
   - Select **Manage**

   ![QuickSight Manage](/images/6/23.png?featherlight=false&width=90pc)

2. Turn off **Account termination protection**  
   - Type: ```confirm```  
   - Select **Delete account**

   ![QuickSight Delete](/images/6/24.png?featherlight=false&width=90pc)
