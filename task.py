import boto3
import argparse

def find_matching_files(s3_bucket_name, substring):
    if not s3_bucket_name or not substring:
        return {
            'statusCode': 400,
            'body': 'Missing s3_bucket_name or substring in the input'
        }
    
    s3 = boto3.client('s3')
    
    try:
        response = s3.list_objects_v2(Bucket=s3_bucket_name)
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error listing objects in bucket {s3_bucket_name}: {str(e)}"
        }
    
    if 'Contents' not in response:
        return {
            'statusCode': 404,
            'body': f"No files found in bucket {s3_bucket_name}"
        }
    
    matching_files = []
    
    for obj in response['Contents']:
        key = obj['Key']
        
        if key.endswith('.txt'):
            try:
                file_content = s3.get_object(Bucket=s3_bucket_name, Key=key)['Body'].read().decode('utf-8')
            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': f"Error reading file {key}: {str(e)}"
                }
            
            if substring in file_content:
                matching_files.append(key)
    
    return {
        'statusCode': 200,
        'body': matching_files
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search for a substring in text files in an S3 bucket.')
    parser.add_argument('s3_bucket_name', type=str, help='The name of the S3 bucket')
    parser.add_argument('substring', type=str, help='The substring to search for in text files')

    args = parser.parse_args()

    result = find_matching_files(args.s3_bucket_name, args.substring)
    print(result)