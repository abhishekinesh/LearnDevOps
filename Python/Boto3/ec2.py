import boto3

client = boto3.resource('ec2')
print(dir(client))
instance = client.create_instances(
    ImageId='ami-0614680123427b75e',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    SecurityGroupIds=['sg-0e124d08f16c3239a'],
    SubnetId='subnet-051c2dd37fc0f62e6',
    TagSpecifications=[  
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'MyEC2-boto3-2'
                }
            ]
        }
    ]
)

# response = client.stop_instances(
#     InstanceIds=['i-04d9916901997fc75']  # Replace with your instance ID
# )
# response = client.start_instances(
#     InstanceIds=['i-04d9916901997fc75']  # Replace with your instance ID
# )


