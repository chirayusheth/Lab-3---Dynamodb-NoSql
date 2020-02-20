# app_create.py
import boto3

def create_table(table_name):
  resp = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
      {
          'AttributeName': 'ipaddr',
          'KeyType': 'HASH'  # Partition key
      },
      {
          'AttributeName': 'req_no',
          'KeyType': 'RANGE'  # Sort key
      }
    ],
    AttributeDefinitions=[
      {
          'AttributeName': 'ipaddr',
          'AttributeType': 'S'
      },
      {
          'AttributeName': 'req_no',
          'AttributeType': 'N'
      }
    ],
    ProvisionedThroughput={
      'ReadCapacityUnits': 10,
      'WriteCapacityUnits': 10
    }
  )
  print(resp)

if __name__ == "__main__":
  dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
  table_name = "WebAccessLog"
  try:
    resp = dynamodb.Table(table_name).load()
    print("Table WebAccessLog already exists")

  except:
    create_table(table_name)
