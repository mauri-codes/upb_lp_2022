import json
# import boto3
# s3 = boto3.client('s3')
def create_bucket(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps("hello from lambda")
    }

def list_buckets(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps("hello from lambda")
    }
