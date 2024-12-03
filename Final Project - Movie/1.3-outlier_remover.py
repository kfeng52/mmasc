
import pandas as pd


# Importing Data
df1 = pd.read_csv('./Final Project - Movie/Cleaned IMDb Movie 1.1.csv')
df2 = pd.read_csv('./Final Project - Movie/Cleaned Rotten 2.2.csv')


def remove_outliers_iqr(df, columns=None):
    if columns is None:
        # Use all numeric columns by default
        columns = df.select_dtypes(include=['number']).columns
    
    df_cleaned = df.copy()
    for col in columns:
        Q1 = df_cleaned[col].quantile(0.25)
        Q3 = df_cleaned[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Filter out outliers for the column
        df_cleaned = df_cleaned[(df_cleaned[col] >= lower_bound) & (df_cleaned[col] <= upper_bound)]
    
    return df_cleaned

df1 = remove_outliers_iqr(df1)
df2 = remove_outliers_iqr(df2)


# Returning the DF to CSV format
df1.to_csv('./Final Project - Movie/Cleaned IMDb Movie 1.2.csv', index=False)
df2.to_csv('./Final Project - Movie/Cleaned Rotten 2.3.csv', index=False)