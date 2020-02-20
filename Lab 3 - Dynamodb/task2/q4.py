import boto3
import functools
from boto3.dynamodb.conditions import Key

def resolver(item):
  return (item["timestamp"].split(":")[0], int(item["bytes"]))

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table = dynamodb.Table("WebAccessLog")
resp = table.query(
  KeyConditionExpression=Key("ipaddr").eq("191.182.199.16"),
)

resol = map(resolver, resp["Items"])

obj = {}
for item in resol:
  try:
    obj[item[0]] += item[1]
  except:
    obj[item[0]] = item[1]

print(obj)
