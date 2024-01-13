import boto3
import json

with open('credentials/credentials.json') as f:
    c = json.load(f)

s3_client = boto3.client('s3', aws_access_key_id=c['aws_access_key_id'], aws_secret_access_key=c['aws_secret_access_key'])
# download all files inside s3://weatherbucket-au/2024-01-13_05-04-17_arcane_grove/ to the local machine
for file in s3_client.list_objects(Bucket='weatherbucket-au', Prefix='2024-01-13_05-04-17_arcane_grove/')['Contents']:
    s3_client.download_file('weatherbucket-au', file['Key'], 'cruft/pred/' + file['Key'].split('/')[-1])
