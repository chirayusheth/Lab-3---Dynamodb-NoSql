import boto3
import json
from boto3.dynamodb.conditions import Key

def queryItem(table_name, val):
  table = dynamodb.Table(table_name)
  response = table.query(IndexName="isbn-index", KeyConditionExpression=Key("isbn").eq(val))
  return response["Items"]

if __name__ == "__main__":
  dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
  print(queryItem("Books", "9781491904244"))
