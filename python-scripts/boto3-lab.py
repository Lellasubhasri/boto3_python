import boto3
import json

s3_client = boto3.client('s3')
ec2_client = boto3.client('ec2')

# response = s3_client.list_buckets()

# #print(json.dumps(response, default=str))

# print(response)

# for buc in response["Buckets"]:
#     print(buc["Name"])


response = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        }
    ]
)
#print(response)
print(json.dumps(response, default=str))

for reser in response["Reservations"]:
    for instance in reser["Instances"]:
        print(f"Instance Id: {instance['InstanceId']}- State: {instance['State']['Name']}")

