import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('some_favourite_books')
response = table.delete_item(
    Key = {
        'Title': 'Brain Droppings',
        'Year': int('1998')
    }
)

import pprint; pprint.pprint(response)