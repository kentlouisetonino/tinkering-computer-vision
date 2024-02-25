# Pandas is a library use for exploring and manipulating data.
# DataFrame holds the type of data you might think of as a table.

import pandas as pd

# File path variable.
melbourne_file_path = './data_melbourne_housing.csv'

# Read the data and store data in DataFrame.
melbourne_dataframe = pd.read_csv(melbourne_file_path)

# Summary of the data in Melbourne data.
melbourne_summary = melbourne_dataframe.describe()

# Print the summary
print(melbourne_summary)
