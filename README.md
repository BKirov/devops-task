Overview
I have created a setup where an AWS Lambda function interacts with an S3 bucket. Here’s a summary of the process:

S3 Bucket Creation:

I have created Amazon S3 bucket to store files. In this case, I  uploaded three text files into the bucket.Files were named text1 text2 and text3 with .txt extension.
The string which we were searching for is : devops-quest , which i have added it in text1 and text3


IAM Role Creation:

I have created an IAM  role. This role allows the Lambda function to access resources, such as the S3 bucket. I configured permissions for this role to read from the S3 bucket.
Lambda Function Creation:

I  developed an AWS Lambda function - python based with boto which is a piece of serverless code that can execute automatically. This Lambda function was programmed to interact with the S3 bucket, such as reading or processing the text files stored in it.

What It Does
S3 Bucket: Stores the text files you want to work with.
IAM Role: Grants the Lambda function the necessary permissions to access the S3 bucket.
Lambda Function: Performs actions based on the files in the S3 bucket, such as processing content or performing operations based on the file data.
This setup enables you to automate tasks and interact with S3 files without managing servers, thanks to the combination of S3, IAM, and Lambda.
