import boto3
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

# Write Code here
dynamodb.create_table(
  TableName="Books",
  KeySchema=[
    {
        'AttributeName': 'publisher',
        'KeyType': 'HASH'  # Partition key
    },
    {
        'AttributeName': 'title',
        'KeyType': 'RANGE'  # Sort key
    }
  ],
  AttributeDefinitions=[
    {
        'AttributeName': 'publisher',
        'AttributeType': 'S'
    },
    {
        'AttributeName': 'title',
        'AttributeType': 'S'
    },
    {
        'AttributeName': 'isbn',
        'AttributeType': 'S'
    }
  ],
  GlobalSecondaryIndexes=[
    {
      'IndexName': 'isbn-index',
      'KeySchema': [
        {
          'KeyType': 'HASH',
          'AttributeName': 'isbn'
        }
      ],
      'Projection': {
        'ProjectionType': 'ALL'
      },
      'ProvisionedThroughput': {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
      }
    }
  ],
  ProvisionedThroughput={
    'ReadCapacityUnits': 10,
    'WriteCapacityUnits': 10
  }
)
