import pandas as pd
import os

def read_cheking_data( path):
    data_file = pd.read_csv(path)
    print(data_file) #seeing that it imported correctly
    return data_file

file_path = "Finacial Product 111\files\record_1.csv"

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

read_cheking_data(get_file_path())

def catorgize():
    




    return