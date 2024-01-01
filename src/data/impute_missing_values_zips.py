import pandas as pd
import numpy as np

def fill_missing_values(input_file_path, output_file_path):
    # Read the CSV file, assuming that the delimiter is a comma
    df = pd.read_csv(input_file_path, delimiter=',')

    # Check if 'median_household_income' column exists
    if 'median_household_income' in df.columns:
        # Replace empty strings and NaN in 'median_household_income' with np.nan
        df['median_household_income'] = df['median_household_income'].replace(['', np.nan], np.nan)
    else:
        print("Column 'median_household_income' does not exist in the file.")

    # Write the updated DataFrame to a new CSV in a different folder
    df.to_csv(output_file_path, index=False, na_rep='NaN')

# Usage
fill_missing_values('//data/external/zips.csv',
                    '//data/processed/'
                    'zip_code_classifications.csv')
