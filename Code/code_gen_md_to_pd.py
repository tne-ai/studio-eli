import pandas as pd
from tne.TNE import TNE
import re

# Initialize TNE object
session = TNE(uid=UID, bucket_name=BUCKET, project=PROJECT, version=VERSION)

# Load markdown file
markdown = session.get_object("inventory-reco.md")

# Extract table from markdown
table_match = re.search(r'\| Style Colour Desc.*?\n(.*?)\n\| **Totals**', markdown, re.DOTALL)
table_str = table_match.group(1)

# Split table into rows
rows = table_str.strip().split('\n')

# Extract column names
column_names = [col.strip() for col in rows[0].split('|')[1:]

# Extract data rows
data_rows = []
# for row in rows[1:]:
#     data_row = [col.strip() for col in row.split('|')[1:-1]]
#     data_rows.append(data_row)

# Create dataframe
# df = pd.DataFrame(data_rows, columns=column_names)

# Improved way to create dataframe
df = pd.DataFrame([row.split('|')[1:-1] for row in rows[1:]], columns=[col.strip() for col in rows[0].split('|')[1:-1]])

# Strip whitespace from values
df = df.apply(lambda x: x.str.strip())

# Convert numeric columns to numeric
numeric_columns = ['Distinct Store Count', 'Max Weeks Selling', 'Total Sales', 'End Inv', 'Total Cost']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Set title and comments
df.title = "Inventory Risk Summary"
df.comments = "Products are selected for the clearance recommendation based on a combined ranking of worst performance"

# Store result
result = tabulate(df, headers="keys", tablefmt="pipe", showindex=False)
