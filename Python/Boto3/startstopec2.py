import boto3

client = boto3.client('ec2')

# response = client.stop_instances(
#     InstanceIds=['i-04d9916901997fc75']  # Replace with your instance ID
# )
# response = client.start_instances(
#     InstanceIds=['i-04d9916901997fc75']  # Replace with your instance ID
# )