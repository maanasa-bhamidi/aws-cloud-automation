# AWS automation with Boto3

## What this project does
This project connects to AWS using python and Boto3 to automate cloud operations. 
It lists all running EC2 instances and all S3 buckets without manually clicking in the AWS console.
Error handling is included so the script does not crash on failures.

## AWS Services Used
- Amazon EC2
- Amazon S3
- AWS IAM(for credentials)

## How to Run
1. Install boto3: pip install boto3
2. Configure AWS CLI: aws Configure
3. Run the script: python aws_automation.py

## What I learned
- How to connect python scripts directly to AWS using Boto3
- How EC2 groups instances into Reservations requiring a double loop
- How to handle AWS error gracefully using try/except