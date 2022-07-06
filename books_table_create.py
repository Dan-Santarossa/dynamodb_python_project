#!usr/bin/env python3.7

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName='some_favourite_books',
    KeySchema=[
        {
            'AttributeName': 'Title',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'Year',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
