# app_batch_write.py
import boto3
import json

def batchWrite(table_name, contents):
  table = dynamodb.Table(table_name)

  with table.batch_writer() as batch:
    for item in contents:
      batch.put_item(Item=item)

if __name__ == "__main__":
  dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

  fd = open("../../data/books/books.json", "r")
  books_obj = json.loads(fd.read())

  obj = books_obj["books"][1:100]
  batchWrite("Books", obj)
