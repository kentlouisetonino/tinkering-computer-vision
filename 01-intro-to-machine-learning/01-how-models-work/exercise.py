# Pandas is a library use for exploring and manipulating data.
# DataFrame holds the type of data you might think of as a table.

import pandas as pd

# File path variable.
melbourne_file_path = './data_melbourne_housing.csv'

# Read the data and store data in DataFrame.
melbourne_df = pd.read_csv(melbourne_file_path)

# Melbourne data sections.
melbourne_summary = melbourne_df.describe()
melbourne_columns_list = melbourne_df.columns

# Print the sections.
print("**DATA SUMMARY**", "\n", melbourne_summary)
print("\n")
print("**DATA COLUMNS LIST**", "\n", melbourne_columns_list)
