
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def read_file(file_path):
    data = pd.read_csv(file_path)
    return data.head
    

file_path = "/Users/kylematheson/Desktop/cse111/project/fake_ csvs/fake_bank_transactions.csv"

data = read_file(file_path)

print(data)