# app_get.py
import boto3
import json

def getItem(table_name, key):
  table = dynamodb.Table(table_name)
  response = table.get_item(Key=key)
  return response["Item"]

if __name__ == "__main__":
  dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
  obj = {
    "title": "Learning JavaScript Design Patterns",
    "publisher": "O'Reilly Media"
  }
  print(getItem("Books", obj))
