import boto3

def lambda_handler(event, context):
    s3_bucket_name = event.get('s3_bucket_name')
    substring = event.get('substring')
    
    if not s3_bucket_name or not substring:
        return {
            'statusCode': 400,
            'body': 'Missing s3_bucket_name or substring in the input'
        }
    
    s3 = boto3.client('s3')
    
    response = s3.list_objects_v2(Bucket=s3_bucket_name)
    
    if 'Contents' not in response:
        return {
            'statusCode': 404,
            'body': f"No files found in bucket {s3_bucket_name}"
        }
    
    matching_files = []
    
    for obj in response['Contents']:
        key = obj['Key']
        
        # Only process text files
        if key.endswith('.txt'):
            file_content = s3.get_object(Bucket=s3_bucket_name, Key=key)['Body'].read().decode('utf-8')
            
            if substring in file_content:
                matching_files.append(key)
    
    return {
        'statusCode': 200,
        'body': matching_files
    }


