import boto3
# i-0867ae8c552b55864
# client = boto3.resource('ec2')
client = boto3.client('ec2')

instance_id = input("Enter the instance id : ")

response = client.describe_instances(
    InstanceIds=[instance_id]  # Replace with your instance ID
)
instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']

print(f"Instance state: {instance_state}")

if instance_state == "stopped":
    response = client.start_instances(
        InstanceIds=[instance_id]  # Replace with your instance ID
    )
    print("Instance started")
elif instance_state == "running":
    response = client.stop_instances(
        InstanceIds=[instance_id]  # Replace with your instance ID
    )
    print("Instance Stopped")
else:
    print("instance is not in running/stopped state , It is still in", instance_state, "state")