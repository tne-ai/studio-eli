import pandas as pd 
from tne.TNE import TNE
from io import BytesIO


session = TNE(uid=UID, bucket_name=BUCKET, project=PROJECT, version=VERSION)

def df_to_excel_with_sdk(df, excel_file_name, session):
    """
    Convert a df to an Excel file and upload it using the custom SDK.

    :param df: the dataframe.
    :param excel_file_name: Desired name for the uploaded Excel file.
    :param session: An instance of the TNE SDK session.
    """
    try:
        # Create an in-memory buffer for the Excel file
        with BytesIO() as buffer:
            # Write the DataFrame to the Excel buffer
            df.to_excel(buffer, index=False, engine='openpyxl')
            buffer.seek(0)  # Reset the buffer pointer to the beginning

            # Upload the buffer content using the SDK
            session.upload_object(excel_file_name, buffer.getvalue())

        return f"Successfully converted to '{excel_file_name}' and uploaded it."
    except Exception as e:
        return f"Error: {e}"

if type(PROCESS_INPUT) is pd.DataFrame:
    if PROCESS_INPUT.empty:
        result = "<EMPTY DATAFRAME>"
    else:
        excel_file_name = 'output.xlsx' 
        # result = df_to_excel_with_sdk(PROCESS_INPUT, excel_file_name, session)
        result = tabulate(PROCESS_INPUT, headers="keys", tablefmt="pipe", showindex=False)
elif type(PROCESS_INPUT) is str:
    result = PROCESS_INPUT 
else:
    result = "<ERROR>" 
