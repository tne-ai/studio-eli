import pandas as pd
from io import StringIO
from tne.TNE import TNE

# Initialize the TNE object
session = TNE(uid=UID, bucket_name=BUCKET, project=PROJECT, version=VERSION)

# Load CSV content from the input
csv_content = PROCESS_INPUT

# Split the content into sections
sections = csv_content.strip().split("\n\n")  # Separate blocks by double newline

# Process the first section (Metrics Table)
metrics_df = pd.read_csv(StringIO(sections[0]))

# Process the second section (Detailed Data Table)
details_df = pd.read_csv(StringIO(sections[1]))

# Save both DataFrames into a single CSV (optional: if merging is required)
merged_output_buffer = StringIO()
metrics_df.to_csv(merged_output_buffer, index=False)
merged_output_buffer.write("\n")  # Add a newline between sections
details_df.to_csv(merged_output_buffer, index=False)
merged_output_buffer.seek(0)

# Convert the merged CSV back to a single DataFrame
merged_df = pd.read_csv(StringIO(merged_output_buffer.getvalue()))

# Upload the file to your SDK
session.upload_object("inventory_summary.csv", merged_df)

# Store the result for further use
result = "done"
