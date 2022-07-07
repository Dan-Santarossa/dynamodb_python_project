import boto3
import json

#calling the dynamodb resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

#creating a table variable with the dynamodb table we created
table = dynamodb.Table('some_favourite_books')

#calling the books.json file as our source file
with open("books.json") as json_file:
    books = json.load(json_file) #takes a file object and returns the json object
    for book in books:
        Title = book['Title']
        Year = int(book['Year'])
        info = book['info']

        print("Adding books:", Title, Year, info)

        table.put_item( #put items into table
           Item={
               'Title': Title,
               'Year': Year,
               'info': info
               
               
            }
        )
 
