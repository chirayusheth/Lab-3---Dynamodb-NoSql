import boto3
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

item = {
  "sha": "K9QTUE0U3SKDFFKFVP7PMTMQF6GZNEB8NSFH1K",
  "author": "lisa",
  "message": "Resolved an issue from pdf.js",
  "project_id": 4243,
  "timestamp": "2020-02-19T20:40:38Z"
}

table = dynamodb.Table("Commits")
table.put_item(Item=item)

table = dynamodb.Table("Issues")
resp = table.update_item(
  Key={
    "title": "No Documentation for installation",
    "repo_id": 4243
  },
  UpdateExpression="SET is_resolved = :is_resolved",
  ExpressionAttributeValues={
    ":is_resolved": True
  },
  ReturnValues="ALL_NEW"
)

print(resp)
# Write Code here
