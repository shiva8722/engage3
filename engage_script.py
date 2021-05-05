import pandas as pd
from urllib.parse import urlparse
import boto3
import requests
from botocore.exceptions import NoCredentialsError
import datetime
import uuid
import gzip

ACCESS_KEY = 'AKIAWFY24OEMYMM3HD65'
SECRET_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'e3-interview'



#converting data the required format using pandas.
print("Process initiated for data conversion")

df = pd.DataFrame(requests.get('https://jsonplaceholder.typicode.com/photos').json())
def get_url_params(url):
    new_photo_id = str(url[0])+'_'+str(url[1])
    title = url[2]
    parsed_url = urlparse(str(url[3]))
    new_url = parsed_url.path
    if parsed_url.query or parsed_url.params:
        new_url += '?'+parsed_url.params+parsed_url.query
    if parsed_url.fragment:
        new_url += '#'+parsed_url.fragment 
    timestamp = datetime.datetime.now().isoformat()
    return new_photo_id+"@#"+title+"@#"+new_url+"@#"+str(timestamp)

df['all_columns'] = df.apply(get_url_params,axis=1)
df[['new_photo_id','title','new_url','timestamp']] = df.all_columns.str.split("@#",expand=True)
final_dataframe = df[['new_photo_id', 'title','new_url','timestamp']]
final_dataframe.to_csv("engage_interview.tsv", sep="\t",index=False)

print("data conversion done successfully")
print("Process of File upload to S3 has started")

#To upload file to S3 bucket.
def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

#To convert .tsv file to gz file(compressed)
with open('engage_interview.tsv', 'rb') as f_in, gzip.open('engage_interview.tsv.gz', 'wb') as f_out:
    f_out.writelines(f_in)

from datetime import datetime
file_path = "{}_{}_{}.{}".format("photos",datetime.today().strftime('%Y_%m_%d'),str(uuid.uuid4()),".tsv.gz")

#calling S3 upload function.
upload_to_aws('engage_interview.tsv.gz', AWS_STORAGE_BUCKET_NAME, file_path)
print("Process of File upload to S3 has ended")