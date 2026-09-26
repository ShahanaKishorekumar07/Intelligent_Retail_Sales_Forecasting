# Intelligent Retail Sales Forecasting and Inventory Optimization System

## Project Overview

The Intelligent Retail Sales Forecasting and Inventory Optimization System is a machine learning based application designed to analyze retail sales data, forecast future demand, and provide inventory reorder recommendations.

The system uses historical sales data to identify demand patterns and helps determine which products require reordering.

## Objectives

- Analyze historical retail sales data
- Perform data preprocessing and exploratory data analysis
- Build a machine learning model for sales forecasting
- Predict future sales demand
- Calculate inventory requirements
- Identify products requiring reorder
- Provide recommended order quantities
- Develop an interactive Streamlit dashboard

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Excel
- Google Colab
- GitHub

## Machine Learning Model

Random Forest Regression is used for sales forecasting.

### Input Features

- Year
- Month
- Day
- Day of Week
- Week of Year
- Previous Day Sales
- Previous 7 Day Sales
- 7 Day Average Sales

### Output

Predicted sales demand.

## Inventory Optimization

The system calculates:

### Average Daily Demand

Average quantity demanded per day for each product.

### Safety Stock

Safety stock is estimated using a percentage of expected future demand.

### Reorder Point

```text
Reorder Point = Lead Time Demand + Safety Stock
