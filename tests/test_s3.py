import boto3
import pytest

def test_s3_bucket_list():
    s3 = boto3.client('s3', region_name='eu-north-1')
    buckets = s3.list_buckets()
    bucket_names = [b['Name'] for b in buckets['Buckets']]
    
    assert 'youssefbucket-2000' in bucket_names, "Bucket non trouvé"

def test_s3_upload_download():
    s3 = boto3.client('s3', region_name='eu-north-1')
    test_content = b"Hello AWS"
    
    s3.put_object(Bucket="youssefbucket-2000", Key="test.txt", Body=test_content)
    
    response = s3.get_object(Bucket="youssefbucket-2000", Key="test.txt")
    body = response['Body'].read()
    
    assert body == test_content
