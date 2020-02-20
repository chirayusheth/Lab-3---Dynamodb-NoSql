import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

def batch_write(table_name, contents):
  table = dynamodb.Table(table_name)
  batch_start = 0
  lcontent = len(contents)
  while True:
    if batch_start > lcontent:
      break

    batch_contents = contents[batch_start:batch_start + 25]
    with table.batch_writer() as batch:
      for item in batch_contents:
        batch.put_item(Item=item)

    batch_start += 25

  print(table.scan())

fd = open("../../data/logs/web_access_log.json", "r")
fd_content = json.loads(fd.read())
batch_write("WebAccessLog", fd_content)

