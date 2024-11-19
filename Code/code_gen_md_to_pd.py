import pandas as pd
from tne.TNE import TNE
from tabulate import tabulate
import re

# Initialize TNE object
session = TNE(uid=UID, bucket_name=BUCKET, project=PROJECT, version=VERSION)

# Load markdown file
markdown = session.get_object("inventory-reco.md")

# Extract table from markdown
# Match the table using more robust regex
table_match = re.search(
    r"(\| Style Colour Desc.*?\n(?:\|.*?\n)+)",  # Match rows of Markdown table
    markdown,
    re.DOTALL,
)

if not table_match:
    raise ValueError("Table not found in the Markdown file.")

table_str = table_match.group(1)

# Split the table into rows
rows = table_str.strip().split("\n")

# Extract column names
column_names = [col.strip() for col in rows[0].split("|")[1:-1]]

# Extract data rows
data_rows = [row.split("|")[1:-1] for row in rows[2:]]  # Skip header and separator rows

# Create DataFrame
df = pd.DataFrame(data_rows, columns=column_names)

# Strip whitespace from all values
df = df.applymap(str.strip)

# Convert numeric columns to numeric
numeric_columns = [
    "Distinct Store Count",
    "Max Weeks Selling",
    "Total Sales",
    "End Inv",
    "Total Cost",
]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

# Set title and comments
df.title = "Inventory Risk Summary"
df.comments = "Products are selected for the clearance recommendation based on a combined ranking of worst performance"

# Store result
result = tabulate(df, headers="keys", tablefmt="pipe", showindex=False)
