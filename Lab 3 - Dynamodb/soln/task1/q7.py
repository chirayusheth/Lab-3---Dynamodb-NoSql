import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table = dynamodb.Table("Books")
resp = table.scan(
  FilterExpression=Attr("pages").gt(300)
)

print(resp["Items"])
