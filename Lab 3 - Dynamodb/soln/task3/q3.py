import boto3
from dateutil import parser
from boto3.dynamodb.conditions import Attr, Key

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

# given 'linux' and 'torvalds' < Repositories
# requires 'project_id' < Commits

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
latest = items[0] if len(items) > 0 else None

for item in items:
  if parser.parse(latest["timestamp"]) < parser.parse(item["timestamp"]):
    latest = item

print("Issue: {}\nAuthor: {}".format(latest["message"], latest["author"]))
