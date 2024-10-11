# Crop Yield Prediction Project Report 🌾

## 1. Introduction

This project aims to develop a predictive model for crop yields, focusing on factors that impact food security, such as climate conditions and socioeconomic data. By leveraging machine learning, the model provides valuable insights for agricultural planning and resource allocation to mitigate food security risks.

---

## 2. Data Sources

The model utilizes a combination of data sources to capture various factors that influence crop yield:
- **FAOSTAT**: Provides agricultural statistics, including crop yield and production data across regions.
- **World Bank**: Supplies socioeconomic indicators such as GDP, rural population, and agricultural land use.
- **Climate Data**: Contains historical rainfall, temperature, and soil moisture data, collected from meteorological sources.

---

## 3. Methodology

### Data Cleaning
1. **Outlier Removal**: Applied the Interquartile Range (IQR) method to remove extreme values in rainfall and yield data.
2. **Handling Missing Values**: Filled missing values using the median for numerical columns to retain data stability.

### Feature Engineering
1. **Seasonal Averages**: Calculated rolling averages for rainfall and temperature data to capture seasonal trends that affect crop yields.
2. **Weather Index**: Created a composite index combining rainfall and temperature data, weighted based on relevance to crop growth cycles.

### Model Training and Evaluation
1. **Model Selection**: Several models were tested, including Linear Regression, Random Forest, and Gradient Boosting. Random Forest was chosen as the final model for its high accuracy and interpretability.
2. **Evaluation Metrics**: Model performance was evaluated using:
   - **Root Mean Square Error (RMSE)**: Measures the model’s predictive accuracy.
   - **Mean Absolute Error (MAE)**: Provides an average error measure.
   - **R² Score**: Indicates the percentage of variance explained by the model.

---

## 4. Results and Findings

### Key Variables
The analysis identified several key predictors of crop yield:
- **Rainfall**: Directly impacts crop growth, with optimal levels being essential for yield maximization.
- **Soil Quality Index**: Strongly correlates with yield, as soil nutrients and texture influence crop health.
- **Temperature Averages**: Affects plant physiology, with both extremes having adverse effects.

### Model Performance
- **Random Forest Model**: Selected based on its superior performance, the Random Forest model achieved an RMSE of 1.83 and an R² Score of 0.91, demonstrating strong predictive accuracy for crop yield forecasting.

### Insights for Food Security
1. **High-Risk Regions**: Analysis of yield patterns revealed regions with insufficient rainfall or poor soil quality that are at risk of yield shortages.
2. **Impact of Climate Variables**: Rainfall variability and extreme temperatures are primary risk factors for yield inconsistency, highlighting the need for adaptive measures in high-risk areas.

---

## 5. Future Work

To improve the model and broaden its applicability, future iterations could consider:
1. **Expanding the Dataset**: Incorporate additional climate indicators, such as humidity and solar radiation, to improve model accuracy.
2. **Deploying as an API**: Develop an API that allows users to input data and receive real-time predictions for crop yields.
3. **Exploring Advanced Models**: Test deep learning models (e.g., LSTM) to capture temporal dependencies in climate data for longer-term forecasts.

---

## Appendix

### A. Visualization Files
- **yield_vs_rainfall.png**: Scatter plot showing the relationship between rainfall and crop yield.
- **actual_vs_predicted_yield.png**: Scatter plot comparing actual and predicted crop yields.

### B. Metrics
- **evaluation_metrics.json**: JSON file with model evaluation scores (RMSE, MAE, R²).

---

## References

- FAOSTAT. (2024). [FAOSTAT - Food and Agriculture Organization](http://www.fao.org/faostat/).
- World Bank. (2024). [World Bank Open Data](https://data.worldbank.org/).
- NOAA. (2024). [Climate Data Online](https://www.ncdc.noaa.gov/cdo-web/).

