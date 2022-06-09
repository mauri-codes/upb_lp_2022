import json
import boto3
dynamodb = boto3.resource('dynamodb')
def adopt(event, context):
    body = json.loads(event["body"])
    pet = body["pet"] # pet_A
    owner = body["owner"] #owner_01
    year = body["year"] #2020
    employee = body["employee"] #emp_a
    table = dynamodb.Table('petStore')
    
    table.put_item(
       Item={
            'pk': owner,
            'sk': pet,
            'employee': employee,
            'year': year
        }
    )
    table.put_item(
       Item={
            'pk': f'{employee}#{owner}#{year}',
            'sk': pet,
            'employee': employee,
            'year': year
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps("data saved")
    }

def adopted_by_owner(event, context):
    
    return {
        'statusCode': 200,
        'body': json.dumps("hello from lambda")
    }

def adopted_by_year(event, context):
    
    return {
        'statusCode': 200,
        'body': json.dumps("hello from lambda")
    }

