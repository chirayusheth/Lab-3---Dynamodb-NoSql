import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

# given '2048' and 'janet' < Repositories
# requires 'repo_id' < Issues

table = dynamodb.Table("Repositories")
resp = table.get_item(
  Key={
    "name": "2048",
    "owner": "janet"
  }
)

repo_id = resp["Item"]["id"]

table = dynamodb.Table("Issues")
resp = table.scan(
  FilterExpression=Attr("repo_id").eq(repo_id) & Attr("is_resolved").eq(False),
)

for item in resp["Items"]:
  print(item["title"])
