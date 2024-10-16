import pandas as pd
import matplotlib.pyplot as plt

def read_financial_data(file_path):
    # Read the CSV file into a DataFrame
    data = pd.read_csv(file_path)
    
    # Display the first few rows of the data
    print(data.head())
    return data

def analyze_spending_trends(data):
    # Plot income vs expenses
    plt.figure(figsize=(10, 5))
    plt.plot(data['Income'], label='Income', color='b')
    plt.plot(data['Expenses'], label='Expenses', color='r')
    plt.xlabel('Entry Index')
    plt.ylabel('Amount ($)')
    plt.title('Income vs Expenses Over Time')
    plt.legend()
    plt.show()
    
    # Calculate average spending
    avg_expenses = data['Expenses'].mean()
    print(f'Average Expenses: ${avg_expenses:.2f}')
    
    # Calculate the savings rate
    data['Savings Rate (%)'] = (data['Savings'] / data['Income']) * 100
    avg_savings_rate = data['Savings Rate (%)'].mean()
    print(f'Average Savings Rate: {avg_savings_rate:.2f}%')

def visualize_monthly_savings(data):
    # Plot monthly savings trends
    plt.figure(figsize=(10, 5))
    plt.plot(data['Savings'], label='Savings', color='g')
    plt.xlabel('Entry Index')
    plt.ylabel('Savings Amount ($)')
    plt.title('Monthly Savings Trends')
    plt.legend()
    plt.show()

# Example usage:
file_path = 'Chase9066_Activity_20241014.CSV'
data = read_financial_data(file_path)
analyze_spending_trends(data)
visualize_monthly_savings(data)