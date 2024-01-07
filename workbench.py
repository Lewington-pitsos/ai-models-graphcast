import time
import boto3
import json
from botocore.exceptions import ClientError
import subprocess

with open('credentials/creds.json') as f:
    credentials = json.load(f)

def execute_ssh_command(host, key_path, command):
    ssh_command = f"ssh -o StrictHostKeyChecking=no -i {key_path} ubuntu@{host} {command}"
    print(f"Executing: {ssh_command}")
    try:
        result = subprocess.run(ssh_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout + result.stderr
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e}"
    
def create_ec2_instance(image_id, instance_type, key_name, security_group_id, region_name='ap-southeast-2'):
    ec2 = boto3.resource('ec2', region_name=region_name)

    instance = ec2.create_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group_id],
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/sda1',
                'Ebs': {
                    'VolumeSize': 90
                }
            }
        ]
        
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


def detach_volume(volume_id, instance_id):
    """
    Detach an EBS volume from an EC2 instance.

    :param volume_id: The ID of the EBS volume to detach.
    :param instance_id: The ID of the EC2 instance.
    :return: True if the volume was successfully detached, False otherwise.
    """
    ec2 = boto3.client('ec2')

    try:
        response = ec2.detach_volume(VolumeId=volume_id, InstanceId=instance_id)
        print(f"Detach request for volume {volume_id} from instance {instance_id} has been sent.")
        print("Response:", response)
        return True
    except ClientError as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == '__main__':
    # # Example parameters
    IMAGE_ID = 'ami-04f5097681773b989'  # Replace with the AMI ID of your choice
    INSTANCE_TYPE = "t2.2xlarge"         # Specify the desired instance type
    KEY_NAME = credentials["aws-key-name"]         # Replace with your key name
    SECURITY_GROUP_ID = credentials["aws-security-group-id"] # Replace with your security group ID

    instance = create_ec2_instance(IMAGE_ID, INSTANCE_TYPE, KEY_NAME, SECURITY_GROUP_ID)
    print(f'Instance created with ID: {instance.id}, connect via {instance.public_dns_name}')

    instance.wait_until_running()
    instance.load()
    print('Waiting for instance to be fully initialized...')

    attach_to = "/dev/xvdf"
    response = attach_volume(instance.id, credentials["volume-id"], attach_to)
    print(f'Volume attached: {response}')
    time.sleep(10)

    # Commands to execute
    mkdir_command = "sudo mkdir /mnt/volume"
    mount_command = f"sudo mount {attach_to}1 /mnt/volume"
    copy_home_command = 'sudo cp -R /mnt/volume/home/ubuntu/ai-models-graphcast /home/ubuntu/'
    copy_ssh_command = 'sudo cp -R /mnt/volume/home/ubuntu/.ssh/* /home/ubuntu/.ssh'

    dns_name = instance.public_dns_name
    aws_key_path = credentials['aws-key-path']
    execute_ssh_command(dns_name, aws_key_path, mkdir_command)
    execute_ssh_command(dns_name, aws_key_path, mount_command)
    execute_ssh_command(dns_name, aws_key_path, copy_ssh_command)
    execute_ssh_command(dns_name, aws_key_path, copy_home_command)
    
    print('Volume mounted and files copied.')

    # New code to unmount and detach the volume
    unmount_command = 'sudo umount /mnt/volume'
    detach_volume_command = lambda volume_id, instance_id: detach_volume(volume_id, instance_id)

    execute_ssh_command(dns_name, aws_key_path, unmount_command)
    print('Volume unmounted')

    # Detaching the volume
    detach_volume_command(credentials["volume-id"], instance.id)
    print('Volume detached')