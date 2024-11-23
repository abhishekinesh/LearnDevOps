import boto3

def list_ec2_instances():
    # Initialize EC2 client
    ec2 = boto3.client('ec2')
    
    # Retrieve instances
    response = ec2.describe_instances()
    
    # Iterate over all instances and print details
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")

# Call the function
if __name__ == "__main__":
    list_ec2_instances()
