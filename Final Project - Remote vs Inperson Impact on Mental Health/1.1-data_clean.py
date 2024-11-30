import numpy as np 
import pandas as pd

# Importing Data
df1 = pd.read_csv('./Final Project - Remote vs Inperson Impact on Mental Health/cleaned_data_1.1.csv')
df2 = pd.read_csv('./Final Project - Remote vs Inperson Impact on Mental Health/raw_data_2.csv')

# Removes certain values from columns
def value_remove(dataframe, column, value):
    new = dataframe.drop(dataframe[dataframe[column] == value].index)
    return new

# Removes any row that has NaN values
def remove_nan_rows(df):
    return df.dropna()

# Drops rows that have NaN's in specific columns
def remove_rows_with_nan(df, column_name):
    return df.dropna(subset=[column_name])

# Replacing values in a column
def replace_unique_values(df, column_name, value_map):
    df[column_name] = df[column_name].replace(value_map) # value map is in the format of a dictionary
    return df

# Cleaning Dataset 1
df1 = value_remove(df1, 'Work_Location', 'Hybrid')

# Cleaning Dataset 2
df2 = df2.drop('comments', axis=1) # removing a specific column
df2 = remove_rows_with_nan(df2, 'remote_work')
df2 = replace_unique_values(df2, 'remote_work', {'No': 'Onsite', 'Yes':'Remote'})
df2 = remove_nan_rows(df2) #optional

# Returning the DF to CSV format
df1.to_csv('./Final Project - Remote vs Inperson Impact on Mental Health/cleaned_data_1.2.csv', index=False)
df2.to_csv('./Final Project - Remote vs Inperson Impact on Mental Health/cleaned_data_2.1.csv', index=False)