import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('some_favourite_books')
#response = table.delete

table.delete()

print("Table status:", table.table_status)