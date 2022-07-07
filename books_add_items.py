import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('some_favourite_books')

with open("books.json") as json_file:
    books = json.load(json_file)
    for book in books:
        Title = book['Title']
        Year = book['Year']
        author = book['author']
        genre = book['genre']

        print("Adding books:", Title, Year, author, genre)

        table.put_item(
           Item={
               'Title': Title,
               'Year': Year,
               'author': author,
               'genre': genre
               
            }
        )
    
