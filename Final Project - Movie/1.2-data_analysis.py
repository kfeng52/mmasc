import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import scipy.stats as stats

# Importing Data
df1 = pd.read_csv('./Final Project - Movie/Cleaned IMDb Movie 1.1.csv')
df2 = pd.read_csv('./Final Project - Movie/Cleaned Rotten 2.2.csv')


# Stats summary for all variables types
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

def categorical_numerical_stats(df, categorical_col, numerical_col, ci=0.95):

    print(f"Statistics for {categorical_col} vs {numerical_col} (CI = {ci * 100:.1f}%):\n")
    print(f"{'Category':<15}{'Mean':<10}{'Median':<10}{'Q1':<10}{'Q3':<10}{'Std Dev':<10}{'Range':<10}{'Min':<10}{'Max':<10}")
    print("-" * 95)
    
    for category, group in df.groupby(categorical_col):
        values = group[numerical_col].dropna()
        mean = values.mean()
        median = values.median()
        q1 = values.quantile(0.25)
        q3 = values.quantile(0.75)
        std_dev = values.std()
        data_range = values.max() - values.min()
        min_val = values.min()
        max_val = values.max()
        sem = stats.sem(values)
        margin_of_error = sem * stats.t.ppf((1 + ci) / 2, len(values) - 1)
        lower_ci = mean - margin_of_error
        upper_ci = mean + margin_of_error
        
        print(f"{category:<15}{mean:<10.2f}{median:<10.2f}{q1:<10.2f}{q3:<10.2f}{std_dev:<10.2f}{data_range:<10.2f}{min_val:<10.2f}{max_val:<10.2f}")


categorical_numerical_stats(df1, 'Motion Picture Rating', 'Rating (Out of 10)')

