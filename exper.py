
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re

def read_cheking_data(path):
    # Read the CSV file
    data_file = pd.read_csv(path)
    print(data_file.head())  # See a preview to ensure it's imported correctly
    return data_file

# Load the CSV file
df = read_cheking_data("/Users/kylematheson/Desktop/cse111/project/fake_ csvs/Chase9066_Activity_20241023.CSV")

# Convert 'Description' or another text column to lowercase (assuming 'Description' contains text data)
details_text = df['Posting Date'].astype(str).str.lower()
print(details_text.head())  # Display a preview of the text column

# Create a CountVectorizer to find bigrams and trigrams (without stop words)
vectorizer = CountVectorizer(ngram_range=(2, 3), stop_words='english')

# Fit the vectorizer and transform the text data into n-grams
ngrams_matrix = vectorizer.fit_transform(details_text)

# Get the list of n-grams and their frequencies
ngram_list = vectorizer.get_feature_names_out()
ngram_frequencies = ngrams_matrix.toarray().sum(axis=0)

# Combine n-grams with their corresponding frequencies into a pandas Series
ngrams_series = pd.Series(ngram_frequencies, index=ngram_list)

# Filter out n-grams that contain any digits using a regular expression
filtered_ngrams = ngrams_series[~ngrams_series.index.str.contains(r'\d')]

# Find the most repeated n-gram
most_repeated = filtered_ngrams.idxmax()
count = filtered_ngrams.max()

# Display the result
print()
print(f"The most repeated n-gram is: '{most_repeated}' with {count} occurrences")


