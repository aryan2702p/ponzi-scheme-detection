import pandas as pd

# Read the original CSV file
original_df = pd.read_csv('Ponzi_contracts.csv')

# Select the first 200 rows
subset_df = original_df.tail(200)

# Write the subset DataFrame to a new CSV file
subset_df.to_csv('subset_file.csv', index=False)
