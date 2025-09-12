---
title : "Connect với webhook bằng postman"
date :  "2025-09-11" 
weight : 2
chapter : false
pre : " <b> 4.2 </b> "
---

#### Connect với webhook

1. Truy cập giao diện Postman: ```https://www.postman.com```
 - Chọn **Workspace**


![Create VPC](/images/4-API/4.2-Postman/1.png?featherlight=false&width=90pc)

2. Tại workspace tạo một tab làm việc mới

![Create VPC](/images/4-API/4.2-Postman/2.png?featherlight=false&width=90pc)

3. Quay lại giao diện **API Gateway**
 - Copy **Invoke URL**: ```https://vdmj0zewl4.execute-api.us-east-1.amazonaws.com```

![Create VPC](/images/4-API/4.2-Postman/3-1.png?featherlight=false&width=90pc)



4. Chọn **Body** 
 - Điền địa chỉ ```https://api.telegram.org/bot<token-botTele>/setWebhook```. **\<token-botTele\>** là link token tạo bot Telegram ban đầu
 - Tại **Key** điền: ```url```
 - Tại **Value** điền: ```https://vdmj0zewl4.execute-api.us-east-1.amazonaws.com/<Lambda-function-name>``` vừa lấy ở bước 3 (Invoke URL)

![Create VPC](/images/4-API/4.2-Postman/3.png?featherlight=false&width=90pc)

5. Nhấn **Send** 
 - Response trả về như trong ảnh là ok

![Create VPC](/images/4-API/4.2-Postman/4.png?featherlight=false&width=90pc)

```Python
{
    "ok": true,
    "result": true,
    "description": "Webhook was set"
}
```