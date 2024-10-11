# src/model_training.py

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import joblib

def split_data(df, target):
    """
    Split data into train and test sets.
    
    Parameters:
    df (DataFrame): DataFrame with features and target.
    target (str): Target variable name.
    
    Returns:
    tuple: X_train, X_test, y_train, y_test datasets.
    """
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    """
    Train a RandomForest model with grid search.
    
    Parameters:
    X_train (DataFrame): Training feature set.
    y_train (Series): Training target set.
    
    Returns:
    model: Best trained model from grid search.
    """
    rf = RandomForestRegressor(random_state=42)
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
    }
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_

# Example usage
if __name__ == "__main__":
    data = pd.read_csv('data/processed/featured_crop_data.csv')
    X_train, X_test, y_train, y_test = split_data(data, target='yield')
    best_model = train_model(X_train, y_train)
    joblib.dump(best_model, 'results/best_model.pkl')
