import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load user financial data
def load_financial_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Split data into training and testing sets
def split_data(data):
    X = data[['Income', 'Expenses']]
    y = data['Savings']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Train the model to predict savings
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Predict future spending patterns
def predict_savings(model, X_test):
    predictions = model.predict(X_test)
    return predictions

# Plot the predictions vs actual data
def plot_predictions(y_test, predictions):
    plt.scatter(y_test, predictions, alpha=0.5)
    plt.xlabel('Actual Savings')
    plt.ylabel('Predicted Savings')
    plt.title('Actual vs Predicted Savings')
    plt.show()

# Example usage:
file_path = 'user_financial_data.csv'

# Load data
data = load_financial_data(file_path)

# Split data
X_train, X_test, y_train, y_test = split_data(data)

# Train model
model = train_model(X_train, y_train)

# Predict savings
predictions = predict_savings(model, X_test)

# Plot predictions
plot_predictions(y_test, predictions)