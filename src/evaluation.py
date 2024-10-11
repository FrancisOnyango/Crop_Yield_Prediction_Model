# src/evaluation.py

import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import matplotlib.pyplot as plt

def load_model(model_path):
    """
    Load a trained model from disk.
    
    Parameters:
    model_path (str): Path to the saved model file.
    
    Returns:
    model: Loaded model.
    """
    return joblib.load(model_path)

def evaluate_model(model, X_test, y_test):
    """
    Evaluate model on test data.
    
    Parameters:
    model: Trained model.
    X_test (DataFrame): Test feature set.
    y_test (Series): Test target values.
    
    Returns:
    dict: Dictionary containing evaluation metrics.
    """
    y_pred = model.predict(X_test)
    metrics = {
        "RMSE": mean_squared_error(y_test, y_pred, squared=False),
        "MAE": mean_absolute_error(y_test, y_pred),
        "R2 Score": r2_score(y_test, y_pred),
    }
    return metrics

def plot_results(y_test, y_pred):
    """
    Plot predicted vs actual values.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.xlabel("Actual Yields")
    plt.ylabel("Predicted Yields")
    plt.title("Actual vs. Predicted Crop Yields")
    plt.show()

# Example usage
if __name__ == "__main__":
    data = pd.read_csv('data/processed/featured_crop_data.csv')
    X_train, X_test, y_train, y_test = split_data(data, target='yield')
    model = load_model('results/best_model.pkl')
    metrics = evaluate_model(model, X_test, y_test)
    print(metrics)
    plot_results(y_test, model.predict(X_test))
