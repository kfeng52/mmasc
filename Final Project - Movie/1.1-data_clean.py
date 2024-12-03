import numpy as np 
import pandas as pd
import re

# Variables 

approved_ratings_list = ['G', 'PG', 'PG-13', 'R']


# Importing Data
df1 = pd.read_csv('./Final Project - Movie/IMDbMovies-Clean.csv')
df2 = pd.read_csv('./Final Project - Movie/Cleaned Rotten 2.1.csv')

# Return a list of unique values in a column 
def unique_values(dataframe, column_name):
    if column_name in dataframe.columns:
        return dataframe[column_name].unique().tolist()
    else:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

# Function to change values in a specific column
def change_column_value(dataframe, column_name, current_value, new_value):
    if column_name in dataframe.columns:
        dataframe[column_name] = dataframe[column_name].replace(current_value, new_value)
        return dataframe
    else:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

# Condenses ratings 
def condense_ratings(dataframe, column_name):
    # Define mapping from ratings to categories
    rating_map = {
        'G': 'G',
        'TV-G': 'G',
        'TV-Y': 'G',
        'TV-Y7': 'G',
        'TV-Y7-FV': 'G',
        'PG': 'PG',
        'TV-PG': 'PG',
        'M': 'PG',
        'M/PG': 'PG',
        'GP': 'PG',
        'T': 'PG',
        'PG-13': 'PG-13',
        '13+': 'PG-13',
        '16+': 'PG-13',
        'R': 'R',
        'TV-MA': 'R',
        'NC-17': 'R',
        'X': 'R',
        '18+': 'R',
        'Not Rated': 'R',
        'Unrated': 'R',
        'Approved': np.nan,
        'Passed': np.nan
    }
    
    # Apply the mapping
    dataframe[column_name] = dataframe[column_name].replace(rating_map)
    
    return dataframe

# Only allows certain values in a column 
def filter_rows_by_values(dataframe, column_name, allowed_values):
    if column_name in dataframe.columns:
        return dataframe[dataframe[column_name].isin(allowed_values)]
    else:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

# Removes rows in a column if empty 
def remove_nan_rows(dataframe, column_name):
    if column_name in dataframe.columns:
        return dataframe[dataframe[column_name].notna()]
    else:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

# Counting Number of People 
def count_commas_and_add_column(dataframe, column_name):
    if column_name in dataframe.columns:
        # Create a new column name
        new_column_name = f"{column_name}_count"
        
        # Count commas in the column and add 1
        dataframe[new_column_name] = dataframe[column_name].apply(lambda x: x.count(',') + 1 if isinstance(x, str) else 1)
        
        return dataframe
    else:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

# Function to convert runtime
def convert_time_to_minutes(dataframe, column_name):
    def time_to_minutes(time_str):
        if isinstance(time_str, str):
            hours = 0
            minutes = 0

            # Extract hours and minutes using regex
            hours_match = re.search(r'(\d+)h', time_str)
            minutes_match = re.search(r'(\d+)m', time_str)

            if hours_match:
                hours = int(hours_match.group(1))
            if minutes_match:
                minutes = int(minutes_match.group(1))

            # Convert to total minutes
            return hours * 60 + minutes
        return 0  # Return 0 if the value is not a string

    # Apply the function to the specified column and create a new column 'time_in_minutes'
    dataframe[column_name + '_minutes'] = dataframe[column_name].apply(time_to_minutes)
    return dataframe

# Converting function to millions
def convert_to_millions(dataframe, column_name):
    def parse_value(value):
        if isinstance(value, str):
            # Remove '$' and handle 'K' or 'M'
            value = value.replace('$', '')  # Remove dollar sign
            try:
                if 'M' in value:
                    return float(value.replace('M', ''))  # Convert millions
                elif 'K' in value:
                    return float(value.replace('K', '')) / 1000  # Convert thousands to millions
                else:
                    return float(value) # Convert raw numbers to millions
            except ValueError:
                return 0.0
        return 0.0
    # Create the new column with the format "<column_name> in millions"
    new_column_name = column_name + ' in millions'
    dataframe[new_column_name] = dataframe[column_name].apply(parse_value)
    return dataframe

### Cleaning Dataset 

# Cleaning IMDb Movie (df1)
df1 = condense_ratings(df1, "Motion Picture Rating")
df1 = filter_rows_by_values(df1, "Motion Picture Rating", approved_ratings_list)
df1 = remove_nan_rows(df1, 'Gross in US & Canada (in millions)')
df1 = remove_nan_rows(df1, 'Budget (in millions)')
df1['box_office'] = df1['Gross in US & Canada (in millions)'] - df1['Budget (in millions)'] # Calculating box office 




# Cleaning Rotten Tomatoes Movie (df2)
df2 = condense_ratings(df2, "rating")
df2 = filter_rows_by_values(df2, "rating", approved_ratings_list)
df2 = remove_nan_rows(df2, 'box_office_(gross_usa)')
df2 = count_commas_and_add_column(df2, 'director')
df2 = count_commas_and_add_column(df2, 'producer')
df2 = count_commas_and_add_column(df2, 'writer')
df2 = count_commas_and_add_column(df2, 'production_co')
df2 = convert_time_to_minutes(df2, 'runtime')
df2 = convert_to_millions(df2, 'box_office_(gross_usa)')

# Returning the DF to CSV format
df1.to_csv('./Final Project - Movie/Cleaned IMDb Movie 1.1.csv', index=False)
df2.to_csv('./Final Project - Movie/Cleaned Rotten 2.2.csv', index=False)