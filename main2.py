
import pandas as pd
import os



def read_cheking_data( path):
    data_file = pd.read_csv(path)
    return data_file

#opens file explorer to accept spending data input
def get_file_path():
    import tkinter as tk
    from tkinter import filedialog

    # Create a root window (it won't be visible)
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open the file dialog and get the selected file's path
    file_path = filedialog.askopenfilename()

    # Print the selected file path
    print(f"Selected file: {file_path}")
    # Example: Normalize the path entered by the user
    return os.path.normpath(file_path)



def catorgize(data_frame = pd.DataFrame):
    #This is all the categories and key words that we are looking for. 
    categories = {
        "Grocery": ["GroceryStore","Walmart","WAL-MART","Kroger", "Costco", "Aldi", "Publix", "Safeway", "Target", "Whole Foods", "Trader Joe's", "H-E-B","WINCO"],
        "Rent": ["Landlord Name", "Rent"],
        "Entertainment": ["Amazon","Netflix", "Spotify", "Movie Theater", "Game Store","Theatres", "Regal Entertainment Group", "Cinemark", "Netflix", "Hulu", "Disney+", "Live Nation", "Universal Studios", "Six Flags","World"],
        "Utilities": ["Electric", "Water", "Gas","Utilities","Utility"],
        "Dining": ["Restaurant Name", "Cafe", "Fast Food Place","Dining", "McDonald", "Burger", "Wendy", "Taco", "KFC", "Subway", "Domino", "Pizza", "Chick-fil-A", "Donut", "Food"]
    }

    #Adding a categories collumn to the dataframe
    data_frame["Category"] = "Uncategorized"

    data_frame.drop(columns=["Details", "Type"], inplace= True)

    # Iterates through every row in the dataframe
    for index, collumn in data_frame.iterrows():
        #Sets the transaction detail equal to that rows description
        transaction_details = str(collumn["Description"])
        
        #then iterates through the entire database of possible categories
        for category, keywords in categories.items():
            if any(keyword in transaction_details for keyword in str(keywords)):
                data_frame.at[index, "Category"] = category
                break

 
    return data_frame



data = get_file_path()
data = read_cheking_data(data)
data = catorgize(data)
data.to_csv('file_name.csv', index=False)
print(data)