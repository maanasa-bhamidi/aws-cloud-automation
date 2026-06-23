import boto3
def connect_to_aws(service,region):
    return boto3.client(service, region_name=region)
def list_running_instances(ec2):
    result = ec2.describe_instances()
    for reservation in result["Reservations"]:
        for instance in reservation["Instances"]:
            if instance["State"]["Name"] == "running":
                  print(instance["InstanceId"], instance["InstanceType"])
def list_s3_bucket(s3):
    response = s3.list_buckets()
    for bucket in response["Buckets"]:
                print(bucket["Name"])
ec2 = connect_to_aws("ec2", "us-east-2")
s3 = connect_to_aws("s3", "us-east-2")
try:
    list_running_instances(ec2)
except Exception as e:
    print("Ec2 error:",e)
try:
    list_s3_bucket(s3)
except Exception as e:
    print("S3 error:",e)