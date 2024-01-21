import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('/Users/pintoza/Desktop/dev/data-science/walmart-proximity/data/finals/final_zips.csv')

# Ensure 'population' is treated as float
df['population'] = df['population'].str.replace(',', '').astype(float)

# Ensure 'median_household_income' is treated as string first, then replace and convert to float
df['median_household_income'] = df['median_household_income'].astype(str).str.replace('[\$,]', '', regex=True)

# Handle missing or invalid 'median_household_income' data
df['median_household_income'] = pd.to_numeric(df['median_household_income'], errors='coerce')
df['median_household_income'].fillna(df['median_household_income'].mean(), inplace=True)

# Create the scatter plot
fig = px.scatter(df,
                 x='median_household_income',
                 y='within_10_miles_count',
                 color='ruca',
                 title='Median Household Income vs. Number of Walmarts by RUCA Class',
                 labels={'median_household_income': 'Median Household Income ($)',
                         'within_10_miles_count': 'Number of Walmarts within 10 Miles'})

# Update layout
fig.update_layout(xaxis_title='Median Household Income ($)',
                  yaxis_title='Number of Walmarts within 10 Miles',
                  coloraxis_colorbar=dict(title='RUCA Class'))
fig.show()
