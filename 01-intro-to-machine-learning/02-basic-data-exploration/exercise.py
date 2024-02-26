import pandas as pd
from datetime import datetime

# Melbourne housing data file path.
melb_file = './data_melbourne_housing.csv'

# Read the melbourne housing data and store the dataframe.
melb_df = pd.read_csv(melb_file)

# Melbourne summary.
melb_summary = melb_df.describe()

# Melbourne columns list.
melb_columns_list = melb_df.columns

# Melbourne rows list.
melb_rows_list = melb_df

# Getting the melbourne maximum year built.
melb_year_built = melb_df["YearBuilt"]
melb_max_year_built_value = melb_df.loc[melb_year_built.idxmax(), 'YearBuilt']

# Problem 2: As of today, how old is the newest home.
current_year = datetime.now().year
newest_home_age = current_year - melb_max_year_built_value
print("NEWEST HOME AGE", "\n", newest_home_age)
