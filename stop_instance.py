import boto3

client = boto3.client('ec2')

# response = client.stop_instances(
#     InstanceIds=['i-03f3abf9ce89c4cd6', 'i-03f3abf9ce89c4cd6' ]
# )

response = client.describe_instances(
    Filters=[
        {
            'Name': 'region',
            'Values': [
                'us-east-1'
            ]
        }
    ]