import boto3
from boto3.dynamodb.conditions import Attr, Key

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table = dynamodb.Table("WebAccessLog")
resp = table.query(
  KeyConditionExpression=Key("ipaddr").eq("188.45.108.168"),
  FilterExpression=Attr("status").ne(200)
)

print(resp["Count"])
