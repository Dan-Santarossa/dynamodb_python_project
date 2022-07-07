import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('some_favourite_books')
response = table.scan()
books = response['Items']

while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items'])

import pprint; pprint.pprint(books)