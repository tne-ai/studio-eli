from tne.TNE import TNE

session = TNE(uid=UID, bucket_name=BUCKET, project=PROJECT, version=VERSION)


if type(PROCESS_INPUT) is str:
    text = PROCESS_INPUT 
else:
    text = "<ERROR>" 

result = text
