import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re

def read_cheking_data(path):
    data_file = pd.read_csv(path)
    print(data_file) #seeing that it imported correctly
    return data_file

df = read_cheking_data("project/fake_ csvs/Chase9066_Activity_20241014.CSV")

# Convert 'Description' to lowercase for consistent results
details_text = df['Posting Date'].astype(str).str.lower()
print(details_text)

# Create a CountVectorizer to find bigrams and trigrams
vectorizer = CountVectorizer(ngram_range=(2, 3), stop_words='english')
ngrams = vectorizer.fit_transform(details_text)

# Get the list of n-grams
ngram_list = vectorizer.get_feature_names_out()

# Filter out n-grams containing any digits using a regular expression
filtered_ngrams = [ngram for ngram in ngram_list if not re.search(r'\d', ngram)]

# Display the top n-grams without numbers
print(filtered_ngrams[:20])


