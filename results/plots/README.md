# Plots Directory
This folder stores all visualizations and charts generated during data analysis and model evaluation.
- `yield_vs_rainfall.png`: Scatter plot showing the relationship between rainfall and crop yield.
- `actual_vs_predicted_yield.png`: Scatter plot comparing actual and predicted crop yields.

import matplotlib.pyplot as plt
import seaborn as sns

def save_plot(x, y, title, filename):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.5)
    plt.title(title)
    plt.xlabel("Actual Yields")
    plt.ylabel("Predicted Yields")
    plt.plot([min(x), max(x)], [min(x), max(x)], 'k--', lw=2)
    plt.savefig(f'results/plots/{filename}')
    plt.close()

# Example usage
y_test = [3.1, 2.8, 3.4]  # Example actual yields
y_pred = [3.0, 2.9, 3.5]  # Example predicted yields
save_plot(y_test, y_pred, "Actual vs Predicted Yields", "actual_vs_predicted_yield.png")
