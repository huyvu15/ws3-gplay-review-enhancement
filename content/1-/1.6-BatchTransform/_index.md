---
title : "Sagemaker Batch Transform"
date :  "2025-09-11" 
weight : 6 
chapter : false
pre : " <b> 1.6 </b> "
---

### Về Sagemaker

![](https://miro.medium.com/v2/resize:fit:1400/1*o-Gim_HB9n8UzRBZHhM9ow.png )

Sagemaker cho phép đơn giản hóa việc triển khai các mô hình học máy một cách dễ dàng. Khi training một model, bạn muốn gọi Sagemaker với một số dữ liệu đầu vào. Tại đây sagemaker cung cấp 4 tùy chọn chi phí và giới hạn:

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*UPAdQ0VLtFe0OPAx.png)

#### Sagemaker Batch Transform 

##### Giới thiệu
SageMaker Batch Transform là dịch vụ suy luận hàng loạt dùng để chạy mô hình ML trên tập dữ liệu có sẵn, lưu kết quả trực tiếp về S3. Phù hợp cho các kịch bản không yêu cầu độ trễ thấp và cần xử lý khối lượng dữ liệu lớn theo lô.

Sử dụng Batch Transform giúp không cần phải duy trì một cái endpoint liên tục và chỉ muốn thực hiện inference cho 1 tập dữ liệu theo thời điểm. Sagemaker Batch Transform serverless, scalable, and cost-effective solution for running batch inferences on large datasets.


=> Sagemaker Batch Transform = ECS + S3

##### Khái niệm
- Chạy inference theo lô thay vì theo yêu cầu thời gian thực.
- Đọc dữ liệu đầu vào từ S3 và ghi kết quả ra S3 dưới dạng file.
- Không cần triển khai Endpoint, chỉ chạy khi có job nên tối ưu chi phí cho xử lý định kỳ.

**Một inference cho một model:**
- model_fn
- input_fn
- predict_fn
- output_fn

**Các thành phần tối thiểu để tạo Sagemaker Batch Transform Job như sau:**
```
sagemaker_client = boto3.client('sagemaker')

request = {
            "TransformJobName": batch_job_name,
            "ModelName": model_name,
            "MaxPayloadInMB": payload_size,
            "BatchStrategy": "MultiRecord",
            "MaxConcurrentTransforms": max_concurrent_tranform_jobs,
            "Environment": environment_variables,
            "TransformInput": {
                "DataSource": {
                    "S3DataSource": {
                        "S3DataType": "S3Prefix",
                        "S3Uri": input_s3_path
                    }
                },
                "ContentType": "text/csv",
                "SplitType": "Line",
                "CompressionType": "None"
            },
            "TransformOutput": {
                'S3OutputPath': output_s3_path,
            },
            "TransformResources": {
                "InstanceType": instance_type,
                "InstanceCount": instance_count
            }
        }
sagemaker_client.create_transform_job(**request)
```
The configuration specifies the following details:

- "TransformJobName": The unique name of the batch transform job.
- "ModelName": The name of the pre-trained model that will be used for the inferences. This model refers to our Docker image to be used while serving the model, produced model artefacts, and environment variables we specified.
- "BatchStrategy": The batch strategy to use for the inferences, which can be either "SingleRecord" or "MultiRecord".
- "MaxConcurrentTransforms": The maximum number of inferences that can be performed concurrently.
- "Environment": A dictionary of environment variables that will be passed to the EC2 instances.
- "TransformInput": The input data for the batch transform job, including the S3 location, data type, content type, and compression type.
- "TransformOutput": The S3 location where the results of the batch transform job will be stored.
- "TransformResources": The EC2 resources to be used for the batch transform job, including the instance type and the number of instances.


#### What Happens After We Created Batch Transform Job?
Dưới đây là các bước mà **AWS Sagemaker** sẽ thực hiện trong quá trình batch transform:

1. **Khởi tạo EC2**  
   Sagemaker sẽ khởi chạy một EC2 instance đặc biệt theo các tham số được chỉ định trong `TransformResources`.

2. **Thiết lập môi trường bằng Docker image**  
   Instance sẽ được cấu hình bằng Docker image mà đối tượng `Model` tham chiếu tới.

3. **Nạp biến môi trường**  
   Sagemaker sẽ nạp các biến môi trường (`environment variables`) vào instance.  
   - Lưu ý: Đối tượng `Model` cũng có thể chứa các biến môi trường riêng.  
   - Nếu cùng một biến môi trường được định nghĩa cả trong `Model` và trong tham số `create_transform_job`, thì giá trị cuối cùng sẽ lấy từ `create_transform_job`.

4. **Kiểm tra sức khỏe (health check)**  
   Sagemaker gửi yêu cầu ping để kiểm tra tình trạng của instance:  
   - Nếu không vượt qua kiểm tra, job sẽ thất bại với trạng thái lỗi.  
   - Nếu thành công, tiến trình sẽ chuyển sang bước tiếp theo.

5. **Xác định dữ liệu đầu vào**  
   Thông qua tham số `TransformInput`, Sagemaker xác định dữ liệu cần xử lý.

6. **Thực hiện dự đoán (inference)**  
   Dựa vào các tham số như `MaxConcurrentTransforms`, `BatchStrategy`, và `MaxPayloadInMB`, Sagemaker bắt đầu gửi dữ liệu đầu vào đến endpoint `/invocation` của instance để thực hiện dự đoán.  
   - Nếu các tham số này không được cung cấp trong `create_transform_job()`, Sagemaker sẽ cố gắng lấy từ endpoint `/execution-parameters` của instance đã được tạo.  
   - Nếu endpoint này không tồn tại, Sagemaker sẽ sử dụng **giá trị mặc định**.  

7. **Lưu kết quả dự đoán**  
   Tất cả kết quả sẽ được lưu lại theo cấu hình trong tham số `TransformOutput`.

8. **Dừng instance**  
   Sau khi hoàn tất, Sagemaker sẽ dừng instance.

##### Lưu ý quan trọng

Sagemaker chia nhỏ dữ liệu đầu vào một cách **mù quáng**, không quan tâm đến logic đặc thù của chúng ta. Điều này có thể gây lỗi nếu dữ liệu có **tiêu đề (header)**, vì chỉ phần đầu tiên giữ lại header, các phần còn lại sẽ mất, dẫn đến job Batch Transform thất bại.  

**Cách khắc phục:**

1. Tránh dùng tên tính năng trong suy luận, chỉ cần giữ đúng **thứ tự cột** giống dữ liệu huấn luyện.  

2. Chia nhỏ dữ liệu thủ công thành nhiều file, mỗi file đều có header, rồi cung cấp nhiều file đó cho Batch Transform (mỗi file đầu vào sẽ có output riêng).  



##### Ứng dụng thực tế
- Gắn nhãn/suy luận cho kho dữ liệu lịch sử (ví dụ: đánh giá ứng dụng đã thu thập trên S3).
- Tạo đặc trưng nâng cao (feature enrichment) cho pipeline phân tích báo cáo.
- Phân loại, phát hiện chủ đề/cảm xúc, lọc nội dung quy mô lớn.
- Chạy lại suy luận theo đợt khi có phiên bản mô hình mới.

##### Quan trọng:

- Batch Transform không hỗ trợ dữ liệu đầu vào dạng CSV có chứa ký tự xuống dòng trong cùng một ô.

- Bạn có thể điều chỉnh kích thước mini-batch bằng cách cấu hình tham số BatchStrategy và MaxPayloadInMB.

- Giá trị MaxPayloadInMB không được vượt quá 100 MB.

- Nếu bạn sử dụng thêm tham số MaxConcurrentTransforms, cần đảm bảo công thức:

<p align="center">
  <code>MaxConcurrentTransforms × MaxPayloadInMB ≤ 100 MB</code>
</p>
