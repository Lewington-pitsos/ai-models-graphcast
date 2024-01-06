import boto3
import json

with open('credentials/creds.json') as f:
    credentials = json.load(f)

def create_ec2_instance(image_id, instance_type, key_name, security_group_id):
    ec2 = boto3.resource('ec2')

    instance = ec2.create_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group_id]
    )
    return instance[0]


def attach_volume(instance_id, volume_id, device):
    ec2 = boto3.client('ec2')
    response = ec2.attach_volume(
        VolumeId=volume_id,
        InstanceId=instance_id,
        Device=device
    )
    return response


if __name__ == '__main__':
    # Example parameters
    IMAGE_ID = 'ami-04f5097681773b989'  # Replace with the AMI ID of your choice
    INSTANCE_TYPE = "t2.2xlarge"         # Specify the desired instance type
    KEY_NAME = credentials["aws-key-name"]         # Replace with your key name
    SECURITY_GROUP_ID = credentials["aws-security-group-id"] # Replace with your security group ID

    instance = create_ec2_instance(IMAGE_ID, INSTANCE_TYPE, KEY_NAME, SECURITY_GROUP_ID)
    print(f'Instance created with ID: {instance.id}')

    # Wait for the instance to be running
    print('Waiting for instance to enter running state...')
    instance.wait_until_running()

    # Attach the volume
    response = attach_volume(instance.id, credentials["volume-id"], "/dev/sdf")
    print(f'Volume attached: {response}')