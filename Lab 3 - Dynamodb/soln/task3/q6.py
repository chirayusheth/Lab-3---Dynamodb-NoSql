import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table = dynamodb.Table("Repositories")
resp = table.get_item(
  Key={
    "name": "linux",
    "owner": "torvalds"
  }
)

project_id = resp["Item"]["id"]

table = dynamodb.Table("Commits")
resp = table.query(
  KeyConditionExpression=Key("project_id").eq(project_id),
)

items = resp["Items"]

for item in items:
  print("message: {}\nauthor: {}\n".format(item["message"], item["author"]))
