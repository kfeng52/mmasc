import numpy as np 
import pandas as pd

# Importing Data
df1 = pd.read_csv('./Final Project - Remote vs Inperson Impact on Mental Health/cleaned_data_1.2.csv')
df2 = pd.read_csv('./Final Project - Remote vs Inperson Impact on Mental Health/cleaned_data_2.1.csv')

def summarize_column(df, column_name):
    if column_name not in df.columns:
        return f"Column '{column_name}' does not exist in the DataFrame."
    
    if pd.api.types.is_numeric_dtype(df[column_name]):
        # Summary for numeric columns
        stats = {
            'Mean': df[column_name].mean(),
            'Median': df[column_name].median(),
            'Standard Deviation': df[column_name].std(),
            'Minimum': df[column_name].min(),
            'Maximum': df[column_name].max(),
            'Count': df[column_name].count(),
            'Missing Values': df[column_name].isna().sum()
        }
    else:
        # Summary for non-numeric columns
        stats = {
            'Unique Values': df[column_name].nunique(),
            'Most Frequent': df[column_name].mode()[0] if not df[column_name].mode().empty else None,
            'Value Counts': df[column_name].value_counts().to_dict(),
            'Count': df[column_name].count(),
            'Missing Values': df[column_name].isna().sum()
        }
    
    return stats


print(summarize_column(df1, 'Mental_Health_Condition'))
