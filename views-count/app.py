import boto3
import json
import os

# Initialize DynamoDB resource and table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    try:
        # Get current visitor count
        response = table.get_item(Key={'ID': 'visitors'})
        
        if 'Item' in response and 'Count' in response['Item']:
            count = int(response['Item']['Count'])  # Ensure 'Count' is an integer
        else:
            count = 0  # Default to 0 if 'visitors' item doesn't exist

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

    except Exception as e:
        # Log the exception and return a 500 error response
        print(f"Error processing request: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

