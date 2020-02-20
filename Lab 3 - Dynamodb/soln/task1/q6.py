import boto3
import json

def updateItem(table_name, keyVal, updatedVal):
  key, value = updatedVal
  table = dynamodb.Table(table_name)
  table.update_item(
    Key=keyVal,
    UpdateExpression="SET #key = :val",
    ExpressionAttributeNames={
      "#key": key,
    },
    ExpressionAttributeValues={
      ":val": value
    }
  )

if __name__ == "__main__":
  dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

  keyVal = {
    "title": "Git Pocket Guide",
    "publisher": "O'Reilly Media"
  }

  updatedVal = ["pages", 268]
  updateItem("Books", keyVal, updatedVal)
