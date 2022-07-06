#!usr/bin/env python3.7

import boto3

#Get the service resource.                        #Set appropriate region
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

#Create the DynamoDB table.
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
            'AttributeName': 'Title',
            'AttributeType': 'S'  #S is for string attribute
        },
        {
            'AttributeName': 'Year',
            'AttributeType': 'N'  #N is for number attibute
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
print("Table status:", table.table_status) #print table status
