
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import re



#opens file explorer to accept spending data input
def get_file_path():
    # Create a root window (it won't be visible)
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open the file dialog and get the selected file's path
    file_path = filedialog.askopenfilename()

    # Print the selected file path
    print(f"Selected file: {file_path}")
    # Example: Normalize the path entered by the user
    data_file = os.path.normpath(file_path)
    
    #Returns data frame
    df = pd.read_csv(data_file, index_col=False)
    return df

def categorize(data_frame=pd.DataFrame()):
    # Define the categories and their associated keywords.
    categories = {
        "Utilities": ["taggngo","electric", "water", "gas", "utilities", "utility", "tuition", "maverick"],
        "Grocery": ["walmart", "kroger", "costco", "aldi", "publix", "safeway", "target", "whole", "trader joe's", "h-e-b", "winco"],
        "Rent": ["landlord", "rent"],
        "Entertainment": ["amazon", "netflix", "spotify", "movie theater", "game store", "theatres", "regal entertainment group", "cinemark", "netflix", "hulu", "disney+", "live nation", "universal studios", "six flags", "world"],
        "Dining": ["pizza" "byui food", "restaurant", "cafe", "fast food place", "dining", "mcdonalds", "burger", "wendy", "taco", "kfc", "subway", "domino", "pizza", "chick-fil-a", "donut", "food"],
        "Tithing": ["jesus", "ch jesuschrist"],
        "Transfers":["paypal","venmo","chase card","transfer"]
    }

    # Add a "Category" column to the DataFrame, initially set to "Uncategorized"
    data_frame["Category"] = "Uncategorized"

    # Function to categorize a single transaction based on keywords
    def categorize_transaction(row):

        transaction_details = str(row["Description"]).lower()  # Convert the description to lowercase
        transaction_details = transaction_details.translate(str.maketrans('', '', '0123456789-'))
    
        # Iterate through the categories and their respective keywords
        for category, keywords in categories.items():
            # Create a regex pattern to match whole words only
            keyword_pattern = r'\b(?:' + '|'.join(map(re.escape, keywords)) + r')\b'
            if re.search(keyword_pattern, transaction_details):
                return category  # Return the matched category
        return "Uncategorized"  # Return a default category if no match

    # Apply the categorize_transaction function to each row in the DataFrame
    data_frame["Category"] = data_frame.apply(categorize_transaction, axis=1)

    return data_frame

def remove_income(data_frame=pd.DataFrame()):
    # Inner function to determine whether to drop a row
    def _remove(row):
        if row["Amount"] > 0:  # Check if the value in 'Description' is greater than 0
            return False  # Mark this row to keep it
        return True  # Mark this row to remove it

    # Apply the filter and keep rows where _remove returns True
    filtered_df = data_frame[data_frame.apply(_remove, axis=1)]
    
    # Return the filtered DataFrame
    return filtered_df


def pi_graph(data_frame):
  # Plot a pie chart of the transactions by category
    category_counts = data_frame["Category"].value_counts()
    
    plt.figure(figsize=(8, 6))
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Spending by Category")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def monthly():
    pass

def main():
    data = get_file_path()
    print()
    print("before_cat:")
    print(data.head())
    data.to_csv('before_cat.csv', index=False)
    data = remove_income(data)
    data = categorize(data)
    pi_graph(data)
    print()
    print("after_cat:")
    print(data.head())
    data.to_csv('after_cat.csv', index=False)

if __name__ == "__main__":
    main()


