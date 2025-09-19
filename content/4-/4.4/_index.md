---
title: "Schedule periodic runs with EventBridge"
date: "2025-09-11"
weight: 4
chapter: false
pre: " <b> 4.4 </b> "
---

### Schedule periodic runs with EventBridge

Everything is ready, however the data is only up to the current point. For the system to operate continuously and always update with the latest data, we need services to schedule and trigger

#### For app_details

1. Access EventBridge

![Create VPC](/images/4/1.png?featherlight=false&width=90pc)

2. Select **Schema**
   - Select **Create Schema**

![Create VPC](/images/4/2.png?featherlight=false&width=90pc)

3. Fill in the information:
   - Schedule name: `daily_chplay_app_details`

![Create VPC](/images/4/3.png?featherlight=false&width=90pc)

4. Set Cron time
   - Select **Cron-based schedule**
   - Select `0 6 * * *`: runs at 6 AM every day
   - In **Flexible time window** select **off**
   - Select Next

![Create VPC](/images/4/4.png?featherlight=false&width=90pc)

Note: **Flexible time window** is the delay time when running jobs. If you select 5 minutes, the job will start 5 minutes later.

5. In **Select target** section:
   - Select **AWS Lambda**
   - Select Lambda function `crawl-app-details-maket-chplay`

![Create VPC](/images/4/5.png?featherlight=false&width=90pc)

6. Select **Next**

![Create VPC](/images/4/6.png?featherlight=false&width=90pc)

7. In the **setting** section:
   - Review everything once
   - Scroll to the bottom
   - Select **Use existing role**
   - Select previously created role: `1-role-d4jxk5zk`
   - Select **Next**

![Create VPC](/images/4/7.png?featherlight=false&width=90pc)

8. Review and create schedule
   - Select **Create schedule**

![Create VPC](/images/4/0.png?featherlight=false&width=90pc)

#### For app_reviews

1. Detail section
   - Schedule name: `weekly_chplay_app_reviews`
   - Select **Recurring schedule**

![Create VPC](/images/4/8.png?featherlight=false&width=90pc)

2. Set Cron time
   - Select **Cron-based schedule**
   - Select `15 6 */7 * *`: runs at 6:15 AM every Sunday of each week
   - In **Flexible time window** select **off**
   - Select Next

![Create VPC](/images/4/9.png?featherlight=false&width=90pc)

3. In **Select target** section:
   - Select **AWS Lambda**
   - Select Lambda function `crawl-review-maket-chplay`

![Create VPC](/images/4/10.png?featherlight=false&width=90pc)

4. Select **Next**

![Create VPC](/images/4/11.png?featherlight=false&width=90pc)

5. In the **setting** section:
   - Review everything once
   - Scroll to the bottom
   - Select **Use existing role**
   - Select previously created role: `1-role-d4jxk5zk`
   - Select **Next**

![Create VPC](/images/4/7.png?featherlight=false&width=90pc)

6. Review and create schedule
   - Select **Create schedule**

![Create VPC](/images/4/0.png?featherlight=false&width=90pc)

⇒ Do the same for the trigger lambda job processing from the sentiment model

With EventBridge, we have successfully set up periodic schedules for both app_details and app_reviews, and can similarly extend to other jobs like sentiment analysis. This scheduling helps the system:

- Automate the data crawling process without manual intervention.

- Ensure continuous updates with the latest data, maintaining accuracy and timeliness.

- Easily scale to many other tasks in the data pipeline.

Thanks to this, the entire data processing flow becomes proactive, stable, and capable of long-term operation. This is one of the important steps to build a more automated and intelligent data analysis system.