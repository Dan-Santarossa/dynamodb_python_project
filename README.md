# dynamodb_python_project

Project B

All code should be inline commented.

Create a DynamoDB table for something of your choosing (e.g. movies, food, games).
Using the Gist (https://gist.github.com/zaireali649/0ec6b90155120cf508223788b7b86efc) as a starting point, use boto3 and Python to add 10 or more items to the table.
Use boto3 and Python to scan the DynamoDB table.

ADVANCED
Use boto3 and Python to query a table, remove an item from a table, create a table, and delete a table.

COMPLEX
Create a lambda function using boto3 and Python to query a table, return an item from a table and remove/delete an item from a table.
Run a test of the lambda function to verify you were able to do all of the previous actions.
Create APIs using API Gateway using the console that will each return query a table, return an item, delete an item by calling your lambda function.
Note: You can reference the following documentation to point you in the right direction. The code they are using is NOT Python so take that into consideration: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html
