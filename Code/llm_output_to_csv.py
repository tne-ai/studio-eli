import pandas as pd
from io import StringIO
from tne.TNE import TNE

# Initialize the TNE object
session = TNE(uid=UID, bucket_name=BUCKET, project=PROJECT, version=VERSION)

# Assume PROCESS_INPUT contains the CSV content as a string
csv_content = PROCESS_INPUT

# Create a DataFrame from the CSV content
df = pd.read_csv(StringIO(csv_content))

# Convert the DataFrame back to CSV format (in memory)
output_buffer = StringIO()
df.to_csv(output_buffer, index=False)
output_buffer.seek(0)  # Reset the buffer to the start

# Upload the in-memory CSV to your SDK
session.upload_object("your_filename.csv", output_buffer.getvalue())

# Store the result for further use
result = csv_content
