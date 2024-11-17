from tne.TNE import TNE
import csv

session = TNE(uid=UID, bucket_name=BUCKET, project=PROJECT, version=VERSION)


if type(PROCESS_INPUT) is str:
    text = PROCESS_INPUT 
else:
    text = "<ERROR>" 

session.upload_object("test_output.txt", text)
