import csv
from io import StringIO
from tne.TNE import TNE

# Initialize the TNE object
session = TNE(uid=UID, bucket_name=BUCKET, project=PROJECT, version=VERSION)

csv_content = PROCESS_INPUT
# Convert the CSV content string into rows
rows = csv_content.strip().split("\n")

# Create an in-memory file-like object
output_buffer = StringIO()

# Write rows to the in-memory CSV file
writer = csv.writer(output_buffer)
for row in rows:
    writer.writerow(row.split(","))

# Reset the buffer position to the beginning
output_buffer.seek(0)

# Upload the in-memory file to your custom SDK
session.upload_object("your_filename.csv", output_buffer.getvalue())
result = csv_content
