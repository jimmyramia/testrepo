'''
Delete contents of s3 bucket (so that delete-stack call will work)
'''
import boto3, sys

if len(sys.argv) == 1:
    print ("must pass the bucketname you want to delete contents from")
    sys.exit()
else:
    bucketname = sys.argv[1]

client = boto3.client('s3')
s3 = boto3.resource('s3')
paginator = client.get_paginator('list_objects_v2')
page_iterator = paginator.paginate(Bucket=bucketname)

for page in page_iterator:
    for item in page['Contents']:
        print ('deleting: ' + item['Key'] + ' from bucket: ' + bucketname)
        s3.Object(bucketname, item['Key']).delete()
