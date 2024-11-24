import boto3

client = boto3.client('s3',region_name='ap-south-1')


# #Create s3 bucket
# response = client.create_bucket(
#     Bucket='abhi-bucket-python-boto3',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'ap-south-1',
#     }
# )



# List s3 bucket
response = client.list_buckets(
    MaxBuckets=123,
)

#Get ACL
# response = client.get_bucket_acl(
#     Bucket='abhi-bucket-python-boto3',
# )

#Delete s3 bucket
# response = client.delete_bucket(
#     Bucket='abhi-bucket-python-boto3',
# )
print(response)