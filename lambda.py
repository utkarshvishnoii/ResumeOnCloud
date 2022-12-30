import boto3,json
#from boto3.dynamodb.conditions import Key

dynamodbClient = boto3.client('dynamodb', 
                    region_name='ap-south-1')

def lambda_handler(event, context):
    
    res = dynamodbClient.update_item(
        TableName = 'Resumedb',
        Key = {
            'id': {
                'S': 'counter'
            }
        },
        UpdateExpression = 'ADD visits :inc',
        ExpressionAttributeValues = {":inc" : {"N": "1"}},
        ReturnValues = 'UPDATED_NEW'
        )
    value = res['Attributes']['visits']['N']
    return {      
            'statusCode': 200,
            'body': value}
