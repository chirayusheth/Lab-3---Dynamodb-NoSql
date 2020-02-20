import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table = dynamodb.Table("Repositories")
resp = table.get_item(
  Key={
    "name": "toml-lang",
    "owner": "github"
  }
)

repo_id = resp["Item"]["id"]

table = dynamodb.Table("Issues")
resp = table.scan(
  FilterExpression=Attr("repo_id").eq(repo_id),
)

items = resp["Items"]

for item in items:
  print("title: {}\nreporter: {}\n".format(item["title"], item["reporter"]))
