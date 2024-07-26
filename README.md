# S3 Text File Substring Search

This project provides a Python script to search for a substring within text files stored in an Amazon S3 bucket. The script uses Boto3 to interact with AWS services.

## Problem Solving Approach

### Understanding the Requirements

1. **Task**: Search for a specific substring in text files stored in an Amazon S3 bucket.
2. **Technologies**:
   - **AWS S3**: For storing text files.
   - **Boto3**: Python SDK for AWS services.
3. **Execution Environment**: Decide between running the script locally or using AWS Lambda.

### Evaluating Options

#### AWS Lambda

**Pros**:
- **Serverless**: No need to manage infrastructure.
- **Scalability**: Automatically scales with the number of requests.
- **Cost-Effective**: Pay only for the compute time you consume.

**Cons**:
- **Cold Start**: Initial invocation may be slow.
- **Resource Limits**: Limited execution time (15 minutes max), memory (3 GB), and disk space (512 MB).
- **Complexity**: Requires setup of deployment pipeline, permissions, and potentially AWS CloudFormation for infrastructure as code.

#### Local Python Script with Boto3

**Pros**:
- **Development Speed**: Faster iteration and debugging.
- **Flexibility**: No resource limits like Lambda, can handle larger data sets and longer execution times.
- **Control**: Full control over the execution environment and dependencies.

**Cons**:
- **Infrastructure Management**: Need to manage the runtime environment, including Python installation and package dependencies.
- **Scalability**: Not inherently scalable like Lambda, though it can be run on scalable infrastructure (e.g., EC2, containers).

### Decision Criteria

1. **Complexity and Time Constraints**: For a quick solution or a prototype, a local Python script might be faster to develop and debug.
2. **Resource Requirements**: If the task involves processing a large number of files or large files that exceed Lambda's limitations, a local script is more suitable.
3. **Execution Duration**: If the task might take longer than Lambda’s execution limit, running locally avoids timeout issues.
4. **Development and Testing**: Local development allows for easier testing and debugging without needing to deploy changes to the cloud.

### Decision

Given these considerations, here's the thought process:

1. **Task Complexity and Execution Time**: The task of searching for a substring in potentially large text files could exceed Lambda's 15-minute execution limit. Running the script locally avoids this issue.
2. **Development Speed**: Developing and debugging locally with Python and Boto3 allows for quicker iteration compared to deploying to Lambda for each change.
3. **Flexibility and Control**: Running the script locally provides more control over the environment, including managing dependencies and handling any unforeseen issues without the constraints imposed by Lambda.

Thus, for this particular task, using a local Python script with Boto3 is a practical choice to quickly develop, test, and run the solution without worrying about AWS Lambda’s limitations.

## Implementation Steps

1. **Set Up Virtual Environment**: Ensures isolation of dependencies.
2. **Install Boto3**: Allows interaction with AWS services.
3. **Configure AWS Credentials**: Provides necessary permissions to access S3.
4. **Implement the Script**: Write a Python script to list objects in the S3 bucket, read their contents, and search for the substring.
5. **Run and Debug Locally**: Easily test and debug the script, iterating quickly on any issues that arise.



# S3 Text File Substring Search

This project provides a Python script to search for a substring within text files stored in an Amazon S3 bucket. The script uses Boto3 to interact with AWS services.

## Prerequisites

- Python 3.x
- AWS account and access keys

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/BKirov/devops-task.git
cd devops-task
``` 
2. Create and Activate a Virtual Environment
   For that purpose you have to run setupenv.sh
``` 
chmod +x setup_env.sh
./setup_env.sh
``` 
The setup_env.sh script will:

Create a virtual environment named myenv.
Activate the virtual environment.
Upgrade pip to the latest version.
Install boto3.

3. Configure AWS Credentials
To allow the script to access your AWS resources, you need to configure your AWS credentials. You can do this by creating a ~/.aws/credentials file with your access keys:

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY

```
Alternatively, you can use environment variables:
```
export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
``` 

And finally you can run the Python script 
``` 
python task.py your-s3-bucket-name your-substring
