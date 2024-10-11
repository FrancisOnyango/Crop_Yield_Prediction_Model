# src/data_cleaning.py

import pandas as pd
import numpy as np

def load_data(filepath):
    """
    Load dataset from a specified filepath.
    
    Parameters:
    filepath (str): Path to the data file (CSV format).
    
    Returns:
    DataFrame: Loaded data as a pandas DataFrame.
    """
    return pd.read_csv(filepath)

def clean_missing_values(df, strategy='mean', columns=None):
    """
    Handle missing values in specified columns of the DataFrame.
    
    Parameters:
    df (DataFrame): The input DataFrame with missing values.
    strategy (str): Strategy for filling missing values - 'mean', 'median', or 'mode'.
    columns (list): List of columns to apply the missing value treatment.
    
    Returns:
    DataFrame: Cleaned DataFrame with missing values handled.
    """
    if columns is None:
        columns = df.columns
    
    for column in columns:
        if strategy == 'mean':
            df[column].fillna(df[column].mean(), inplace=True)
        elif strategy == 'median':
            df[column].fillna(df[column].median(), inplace=True)
        elif strategy == 'mode':
            df[column].fillna(df[column].mode()[0], inplace=True)
    
    return df

def remove_outliers(df, columns, threshold=1.5):
    """
    Remove outliers using the IQR method.
    
    Parameters:
    df (DataFrame): The input DataFrame.
    columns (list): List of columns for outlier removal.
    threshold (float): IQR multiplier for defining outliers.
    
    Returns:
    DataFrame: DataFrame with outliers removed.
    """
    for column in columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (IQR * threshold)
        upper_bound = Q3 + (IQR * threshold)
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    
    return df

# Example usage
if __name__ == "__main__":
    data = load_data('data/raw/crop_data.csv')
    data = clean_missing_values(data, strategy='mean', columns=['rainfall', 'temperature'])
    data = remove_outliers(data, columns=['yield', 'rainfall'])
    data.to_csv('data/processed/cleaned_crop_data.csv', index=False)
