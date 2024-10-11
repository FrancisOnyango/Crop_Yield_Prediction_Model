# src/feature_engineering.py

import pandas as pd

def create_seasonal_avg(df, column, period):
    """
    Create a seasonal moving average for a given column.
    
    Parameters:
    df (DataFrame): Input DataFrame.
    column (str): Column to calculate the moving average.
    period (int): Number of periods for the moving average.
    
    Returns:
    DataFrame: DataFrame with a new seasonal average column.
    """
    new_col = f"{column}_seasonal_avg"
    df[new_col] = df[column].rolling(window=period, min_periods=1).mean()
    return df

def create_weather_index(df, temp_col, rain_col):
    """
    Generate a custom weather index combining temperature and rainfall.
    
    Parameters:
    df (DataFrame): Input DataFrame.
    temp_col (str): Column with temperature data.
    rain_col (str): Column with rainfall data.
    
    Returns:
    DataFrame: DataFrame with a new weather index column.
    """
    df['weather_index'] = (df[temp_col] * 0.4) + (df[rain_col] * 0.6)
    return df

# Example usage
if __name__ == "__main__":
    data = pd.read_csv('data/processed/cleaned_crop_data.csv')
    data = create_seasonal_avg(data, 'rainfall', period=12)
    data = create_weather_index(data, 'temperature', 'rainfall')
    data.to_csv('data/processed/featured_crop_data.csv', index=False)
