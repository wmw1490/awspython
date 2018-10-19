import boto3
import sys
import click

session = boto3.Session()
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys to websites"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all S3 buckets"

#    print(sys.argv) # print the args passed on the command line
#    input()
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List objects in an S3 bucket"

    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == '__main__':
    cli()
            