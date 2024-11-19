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
# Use the first row as the header and skip invalid rows like "Totals"
details_section = StringIO("\n".join([row for row in sections[1].splitlines() if "Totals" not in row]))
details_df = pd.read_csv(details_section)

# Save both DataFrames into a single CSV
merged_output_buffer = StringIO()
metrics_df.to_csv(merged_output_buffer, index=False)
merged_output_buffer.write("\n")  # Add a newline between sections
details_df.to_csv(merged_output_buffer, index=False)
merged_output_buffer.seek(0)

# Convert the merged CSV back to a single DataFrame
merged_df = pd.read_csv(StringIO(merged_output_buffer.getvalue()))

# Convert the merged DataFrame to a CSV string
# final_csv = merged_df.to_csv(index=False)

# Upload the CSV string to your SDK
session.upload_object("inventory_summary.csv", merged_df)

# Store the result for further use
result = "done"
