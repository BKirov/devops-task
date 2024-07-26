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
