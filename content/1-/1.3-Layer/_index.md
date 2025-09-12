---
title : "Layer"
date :  "2025-09-11" 
weight : 3 
chapter : false
pre : " <b> 1.3 </b> "
---


#### Về Layer

![Layer](/images/1-Introduce/layer.png?featherlight=false&width=40pc)


- Layer ở đây là các package, bên ngoài các method gốc của ngôn ngữ lập trình thông thường. Để đơn giản hãy tưởng tượng layer tương tự như các thư viện trong python và mình chỉ việc import vào và sử dụng nó như bình thường(mặc định lambda function không có sẵn các thư viện mà phải thêm vào thông qua layers).
- Mỗi Lambda function được add tối đa 5 layers.
- Một lambda function không thể thêm nhiều layer quá số bit cho trước nếu thêm quá sẽ hiện cảnh báo đỏ.


 
- Có 2 cách để thêm layer:
    + Thêm trực tiếp bằng cách zip các file trong thư viện gốc rồi đẩy lên layer (tốn thời gian để nén và có khi ko ăn với lambda hoặc cũng có thể zip thiếu).
    + Cũng zip lại và tải trực tiếp vào lambda function.
    + The layer bằng cách copy ARNs(của những người đã tạo trước đó) cùng với version tương ứng.

Link ARNs tham khảo: **```https://github.com/keithrozario/Klayers```**



