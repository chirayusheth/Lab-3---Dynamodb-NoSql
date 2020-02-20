import boto3
import json

def putItem(table_name, content):
  table = dynamodb.Table(table_name)
  response = table.put_item(Item=content)
  return response

if __name__ == "__main__":
  dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

  fd = open("../../data/books/books.json", "r")
  books_obj = json.loads(fd.read())
  obj = books_obj["books"][0]
  print(putItem("Books", obj))
