import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

# Importing Data
df1 = pd.read_csv('./Final Project - Remote vs Inperson Impact on Mental Health/cleaned_data_1.2.csv')
df2 = pd.read_csv('./Final Project - Remote vs Inperson Impact on Mental Health/cleaned_data_2.1.csv')


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

# Function for bar graph

def single_bar_graph(df, category_col, title='Bar Graph', xlabel=None, ylabel='Count'):
    """
    Creates a single bar graph for counts of a categorical column.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
        category_col (str): The column to count and plot.
        title (str): Title of the bar graph (default: 'Bar Graph').
        xlabel (str): Label for the x-axis (default: None, uses column name).
        ylabel (str): Label for the y-axis (default: 'Count').

    Returns:
        None: Displays the bar graph.
    """
    # Check if the column exists
    if category_col not in df.columns:
        raise ValueError(f"Column '{category_col}' not found in the DataFrame.")
    
    # Count occurrences of each unique value in the column
    counts = df[category_col].value_counts()

    # Plot the bar graph
    plt.figure(figsize=(8, 5))
    plt.bar(counts.index, counts.values, color='skyblue', edgecolor='black')

    # Add labels and title
    plt.title(title)
    plt.xlabel(xlabel if xlabel else category_col)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')

    # Annotate bar heights
    for i, value in enumerate(counts.values):
        plt.text(i, value + 0.5, str(value), ha='center', va='bottom')

    # Show the plot
    plt.tight_layout()
    plt.show()

def analyze_by_category(df, categorical_col, numerical_col):
    """
    Performs statistical analysis for a numerical column grouped by a categorical column.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        categorical_col (str): The column with categorical values (e.g., onsite/offsite).
        numerical_col (str): The numerical column to analyze.

    Returns:
        pd.DataFrame: A summary table with statistics for each category.
    """
    # Check if the columns exist
    if categorical_col not in df.columns or numerical_col not in df.columns:
        raise ValueError(f"Columns '{categorical_col}' or '{numerical_col}' not found in the DataFrame.")
    
    # Handle missing values (optional, depending on your needs)
    df = df.dropna(subset=[categorical_col, numerical_col])
    
    # Group by the categorical column and calculate statistics
    summary = df.groupby(categorical_col)[numerical_col].agg(
        mean='mean',
        median='median',
        std='std',
        min='min',
        max='max',
        count='count'
    ).reset_index()

    return summary

def analyze_two_categoricals(df, cat_col1, cat_col2, numerical_col=None):
    """
    Performs analysis for two categorical columns and optionally a numerical column.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        cat_col1 (str): The first categorical column (e.g., onsite/offsite).
        cat_col2 (str): The second categorical column (e.g., type of disability).
        numerical_col (str, optional): The numerical column to analyze. Defaults to None.

    Returns:
        pd.DataFrame: A summary table with counts (and numerical stats if numerical_col is provided).
    """
    # Check if required columns exist
    required_cols = [cat_col1, cat_col2]
    if numerical_col:
        required_cols.append(numerical_col)
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in the DataFrame.")
    
    # Handle missing values
    df = df.dropna(subset=required_cols)

    # Group by the two categorical columns
    group_cols = [cat_col1, cat_col2]
    if numerical_col:
        summary = df.groupby(group_cols).agg(
            count=('index', 'count'),  # Count of rows in each group
            sum=(numerical_col, 'sum'),
            mean=(numerical_col, 'mean'),
            median=(numerical_col, 'median'),
            std=(numerical_col, 'std'),
            min=(numerical_col, 'min'),
            max=(numerical_col, 'max')
        ).reset_index()
    else:
        # Only count if no numerical column is provided
        summary = df.groupby(group_cols).size().reset_index(name='count')
    
    return summary



sns.boxplot(data=df1, x='Work_Location', y='Number_of_Virtual_Meetings')
plt.show()

#print(analyze_two_categoricals(df2, "remote_work", 'seek_help'))


#analyze_two_categoricals(df1, 'Work_Location', 'Mental_Health_Condition')