---
title : "Crawl data"
date :  "2025-09-11" 
weight : 2 
chapter : false
pre : " <b> 1.2 </b> "
---

#### Crawl data

![](https://tenten.vn/tin-tuc/wp-content/uploads/2023/06/Crawl-la-gi.png)

Crawl data là quá trình tự động thu thập thông tin từ các trang web trên Internet. Để hiểu cách nó hoạt động, hãy tưởng tượng rằng bạn có một bot trên mạng Internet, nhiệm vụ của nó là cứ nhìn thấy cái gì có ích thì mang về.

Bot bắt đầu bằng việc điều hướng qua các trang web, như một người du lịch dạo chơi qua các con đường trên bản đồ. Khi bot đến một trang web, nó quét qua nội dung của trang đó, tìm kiếm các phần tử trong DOM, bot phân tích các phần tử của trang web như các liên kết, văn bản, hình ảnh, video, và dữ liệu cấu trúc.

Sau đó, bot thu thập dữ liệu từ các phần của trang web chứa thông tin bạn quan tâm, như việc bạn ghi chú lại những điều quan trọng khi đọc sách. Dữ liệu này có thể là văn bản, hình ảnh, video, hoặc dữ liệu có cấu trúc như bảng biểu.

Quá trình này được lặp lại cho đến khi bot đã thu thập đủ thông tin hoặc đã truy cập qua tất cả các trang web trong danh sách. Đối với những trang web thường xuyên cập nhật thông tin, bạn có thể lập lịch cho bot để thực hiện lại quá trình crawl định kỳ để đảm bảo dữ liệu của bạn luôn cập nhật.

Tuy nhiên, việc crawl data cần phải được thực hiện cẩn thận và tuân thủ các quy định về bản quyền và chính sách riêng tư của các trang web. Vi phạm các quy định này có thể dẫn đến hậu quả pháp lý. Lời khuyên là nên check file robots.txt trước khi crawl.

Một dân cào dữ liệu chuyên nghiệp sẽ luôn định nghĩa "Cứ cái gì nhìn thấy trên web thì đều có thể lấy về bằng code được".

#### Các phương pháp để crawl data

##### Dùng Ai
Với sự nổi lên của các mô hình ngôn ngữ lớn thì việc crawl bằng Ai có lẽ cũng chẳng xa lạ gì?

**Nổi bật với:**

- Firecrawl
- Apify
- Rapid
- Data Miner

=> Thuận tiện nhanh gọn tuy nhiên sẽ phải trả phí để sử dụng
#### Truyền thống

- Puppeteer
- Selenium
- Scrapy
- Bs4
- Playwright

=> Khó dùng, phải code và dựng hạ tầng để sử dụng