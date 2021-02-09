import boto3

s3 = boto3.client('s3')
s3.upload_file('s3_file.txt','codekraft-login-credentials','demo_file.txt')