import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    # Get current visitor count
    response = table.get_item(Key={'ID': 'visitors'})

    if 'Item' in response:
        count = response['Item']['Count']
    else:
        count = 0

    # Increment visitor count
    count += 1
    table.put_item(Item={'ID': 'visitors', 'Count': count})

    # Return updated count as response
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Headers': '*',
        },
        'body': json.dumps({'count': count})
    }
