from tne.TNE import TNE
import csv
import pandas as pd
from tabulate import tabulate

session = TNE(uid=UID, bucket_name=BUCKET, project=PROJECT, version=VERSION)

if type(PROCESS_INPUT) is pd.DataFrame:
    if PROCESS_INPUT.empty:
        text = "<EMPTY DATAFRAME>"
    else:
        text = tabulate(PROCESS_INPUT, headers="keys", tablefmt="pipe", showindex=False)
elif type(PROCESS_INPUT) is str:
    text = PROCESS_INPUT 
else:
    text = "<ERROR>" 

session.upload_object("test_output4.txt", text)
result = text
