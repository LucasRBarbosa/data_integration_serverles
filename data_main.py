import json
import boto3


def lambda_handler(event, context):

    print(event)

    if 'endpoint' in event['queryStringParameters']:

        input = event['queryStringParameters']

        client = boto3.client('lambda')

        resource = client.invoke(
            FunctionName='arn:aws:lambda:us-east-1:581577752758:function:cortex-dev-submain',
            InvocationType='Event',
            Payload=json.dumps(input)
        )

        return {
            'statusCode': 200,
            'body': "Hello from Lambda!"
        }

    else:

        return {
            'statusCode': 403,
            'body': "He is dead Jim"
        }
