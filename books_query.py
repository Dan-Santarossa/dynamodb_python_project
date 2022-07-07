import boto3

from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('some_favourite_books')

response = table.query(
    KeyConditionExpression=Key('Title').eq('Dune')
)

import pprint; pprint.pprint(response)