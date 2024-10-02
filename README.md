# Cloud Resume Challenge

## Project Overview

This project is part of the **Cloud Resume Challenge**, where I built a resume website using a fully serverless architecture on AWS. The project integrates a frontend hosted on S3 and CloudFront with a backend that uses DynamoDB and AWS Lambda. It also features a visitor counter to track the number of people viewing the resume, which is stored in DynamoDB and updated dynamically using AWS Lambda.

### Architecture Overview

![Architecture Diagram](path-to-diagram)

The architecture consists of two main sections:

- **Frontend**: The resume website is hosted on **Amazon S3**, served via **Amazon CloudFront**, and secured with **AWS Certificate Manager (ACM)** for SSL.
- **Backend**: The visitor count functionality is powered by **AWS Lambda**, **API Gateway**, and **Amazon DynamoDB**.

### Key AWS Services Used:

- **Amazon S3**: To host the static files (HTML, CSS, JS) for the resume website.
- **Amazon CloudFront**: For content delivery and SSL termination.
- **AWS Lambda**: To process and update visitor counts.
- **Amazon API Gateway**: Exposing the Lambda function as an API to fetch and update visitor counts.
- **Amazon DynamoDB**: To store the visitor count.
- **AWS Certificate Manager (ACM)**: To manage the SSL certificate and enable HTTPS.
- **Route 53**: For DNS management, pointing the custom domain to CloudFront.

## Problem Solved

The goal of the challenge was to deploy a dynamic, cloud-native resume that demonstrates key AWS serverless technologies. This project solves the following challenges:

1. **Scalability**: The use of **S3** and **CloudFront** ensures that the website can scale to handle large amounts of traffic without manual intervention.
2. **Automation**: Deployment and infrastructure are fully automated using **AWS SAM (Serverless Application Model)**, allowing for consistent and repeatable deployments.
3. **Real-Time Visitor Tracking**: By using **DynamoDB** and **AWS Lambda**, the website dynamically tracks and updates the visitor count in real-time.

## Deployment Process

### SAM Template Highlights

The infrastructure was deployed using AWS SAM (Serverless Application Model), which simplifies the process of deploying serverless applications.

```yaml
Resources:
  MyWebsite:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: my-resume-site
      WebsiteConfiguration:
        IndexDocument: index.html

  CloudFrontOAI:
    Type: AWS::CloudFront::CloudFrontOriginAccessIdentity

  MyDynamoDBTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: cloud-resume-table
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: ID
          AttributeType: S
      KeySchema:
        - AttributeName: ID
          KeyType: HASH

  ViewsCountFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: ./src/
      Handler: app.lambda_handler
      Runtime: python3.9
      Environment:
        Variables:
          TABLE_NAME: cloud-resume-table
```

### Deployment Steps

1. **Frontend (S3 + CloudFront)**: The static resume website is uploaded to S3, and CloudFront is used to distribute the content globally with SSL protection from ACM.
2. **Backend (API + DynamoDB + Lambda)**: The Lambda function fetches and updates the visitor count in DynamoDB via an API Gateway endpoint.
3. **Infrastructure as Code**: AWS SAM was used to define and deploy all resources in the stack, ensuring that the infrastructure is version-controlled and easily deployable.

## Issues Faced and Solutions

### 1. **CORS Issue with API Gateway**
   - **Problem**: When the frontend attempted to make a request to the API Gateway to fetch the visitor count, I encountered CORS (Cross-Origin Resource Sharing) errors.
   - **Solution**: To resolve this, I updated the Lambda function to include the appropriate CORS headers in its response.

### 2. **SSL Certificate Validation**
   - **Problem**: The SSL certificate issued by AWS ACM wasn't validating due to DNS issues.
   - **Solution**: I configured Route 53 to automatically create DNS validation records, allowing ACM to validate and issue the certificate successfully.

### 3. **Visitor Count Initialization**
   - **Problem**: On initial deployment, DynamoDB didn’t contain a visitor count entry, causing the function to fail.
   - **Solution**: I added logic in the Lambda function to initialize the visitor count to `0` if no record was found in DynamoDB.

## Key Takeaways

- **Serverless Expertise**: This project deepened my understanding of AWS serverless technologies like Lambda, API Gateway, DynamoDB, and CloudFront.
- **Automation with SAM**: Using AWS SAM to automate the infrastructure deployment helped ensure consistency across environments and simplified future updates.
- **Security**: I implemented SSL using AWS Certificate Manager, ensuring secure communication over HTTPS.

## Conclusion

The Cloud Resume Challenge was an excellent learning experience, showcasing the power of AWS serverless technologies. By building and deploying a resume website in a scalable and secure way, I gained valuable insights into cloud architecture, automation, and problem-solving in the cloud.
