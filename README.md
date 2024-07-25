# AWS Lambda with S3 Bucket Using AWS SAM

This project demonstrates how to create an AWS Lambda function that searches for a specific substring in text files stored in an S3 bucket using AWS SAM (Serverless Application Model).

## Prerequisites

- AWS CLI installed and configured
- AWS SAM CLI installed
- An AWS account

## Setup Instructions

### 1. Create an S3 Bucket and Upload Text Files

1. **Create an S3 Bucket**:
   - Go to the AWS Management Console.
   - Navigate to S3 and click on "Create bucket."
   - Enter a unique bucket name (e.g., `devops-quest`), choose the region, and create the bucket.

2. **Upload Text Files**:
   - Click on your new bucket name to open it.
   - Click on "Upload" and add your text files.
   - Follow the prompts to upload the files to the bucket.

### 2. Create and Deploy Lambda Function Using SAM

1. **Initialize a SAM Project**:
   - Open your terminal and run the following command to create a new SAM project:

     ```sh
     sam init
     ```

   - Follow the prompts to select a runtime (e.g., Python) and a project template (e.g., "Hello World Example").

2. **Add Existing Files**:
   - Replace the auto-generated `app.py` with your existing `lambda_function.py`.
   - Replace the auto-generated `template.yaml` with your existing `template.yaml`.

3. **Build the SAM Application**:
   - Run the following command to build your SAM application:

     ```sh
     sam build
     ```

4. **Deploy the SAM Application**:
   - Run the following command to deploy your SAM application. The `--guided` flag will help you configure the deployment interactively:

     ```sh
     sam deploy --guided
     ```

   - Follow the prompts to configure the stack name, AWS region, and other deployment settings. Make sure to allow SAM to create roles with required permissions.

### 3. Testing the Lambda Function

1. **Invoke the Lambda Function**:
   - You can test the deployed Lambda function using the AWS Management Console or the AWS CLI.

   - To test using the AWS CLI, run the following command:

     ```sh
     aws lambda invoke \
       --function-name DevOpsQuestFunction \
       --payload '{"s3_bucket_name": "devops-quest", "substring": "your-substring"}' \
       output.json
     ```

   - Replace `DevOpsQuestFunction` with the name of your deployed function and `"your-substring"` with the substring you want to search for.

2. **Check the Output**:
   - The response will be saved in `output.json`. Open this file to see the list of files containing the specified substring.

## Summary

1. **S3 Bucket Creation**:
   - Created an S3 bucket and uploaded text files.
2. **SAM Project Initialization**:
   - Initialized a new SAM project with `sam init`.
3. **Add Existing Files**:
   - Replaced the auto-generated files with your existing `lambda_function.py` and `template.yaml`.
4. **Build and Deploy**:
   - Built and deployed the SAM application with `sam build` and `sam deploy --guided`.
5. **Test the Function**:
   - Tested the Lambda function using AWS CLI.

By following these steps, you can use AWS SAM to streamline the creation, deployment, and testing of your Lambda function and associated resources.



##IAC AWS CDK Alternative
Step 1: Setting up the AWS CDK Project
Install AWS CDK:

```
npm install -g aws-cdk
```
Create a new CDK project:

```
mkdir s3-search-script
cd s3-search-script
cdk init app --language python
```
Install necessary dependencies:

```
pip install aws-cdk.aws-s3 boto3
```
Step 2: Define the Infrastructure using CDK
Create a stack to define an S3 bucket:

lib/s3_search_script_stack.py

```
from aws_cdk import (
    aws_s3 as s3,
    core
)

class S3SearchScriptStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.bucket = s3.Bucket(self, 
            "SearchBucket",
            versioned=True,
            removal_policy=core.RemovalPolicy.DESTROY 
        )
```
Step 3: Write the script to search for the substring in the S3 bucket
bin/search_s3.py

```
import boto3

def search_in_bucket(bucket_name, substring):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' not in response:
        print(f"No files found in bucket {bucket_name}")
        return []

    matching_files = []

    for obj in response['Contents']:
        file_key = obj['Key']
        file_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_content = file_obj['Body'].read().decode('utf-8')
        if substring in file_content:
            matching_files.append(file_key)

    return matching_files

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Search for a substring in S3 bucket files.')
    parser.add_argument('s3_bucket_name', type=str, help='The name of the S3 bucket')
    parser.add_argument('substring', type=str, help='The substring to search for')
    args = parser.parse_args()

    matches = search_in_bucket(args.s3_bucket_name, args.substring)
    if matches:
        print("Files containing the substring:")
        for match in matches:
            print(match)
    else:
        print("No files found containing the substring.")
```


Step 4: Deploy the infrastructure and run the script
Deploy the CDK stack:

```
cdk deploy
```
Run the script:

```
python bin/search_s3.py <bucket-name> <substring>
```
