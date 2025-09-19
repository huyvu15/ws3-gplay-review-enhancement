---
title : "Layer"
date :  "2025-09-11" 
weight : 3 
chapter : false
pre : " <b> 1.3 </b> "
---

#### About Layer

![Layer](/images/1-Introduce/layer.png?featherlight=false&width=40pc)

- A **Layer** here refers to packages that extend beyond the built-in methods of the programming language.  
  To simplify: you can think of a layer as similar to Python libraries—you just import them and use them as usual.  
  (By default, AWS Lambda functions don’t include external libraries; you must add them through layers).  

- Each Lambda function can include **up to 5 layers**.  

- A Lambda function cannot exceed the maximum size limit for layers. If it does, AWS will show a red warning.  

---

- There are two ways to add a layer:  
  + Upload directly: zip the original library files and push them to a layer (time-consuming, may cause compatibility issues with Lambda, or risk missing files when zipping).  
  + Upload a zipped package directly into the Lambda function.  
  + Use existing layers: copy **ARNs** (from layers others have created) along with the corresponding version.  

Reference ARN repository: **```https://github.com/keithrozario/Klayers```**
