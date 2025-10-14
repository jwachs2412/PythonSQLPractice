import re
from example_pandas import df

# Function to clean text data

def clean_text(text):
    text = text.lower() # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text) # Remove punctuation
    return text

# Apply the cleaning function to the position column

df['cleaned_positions'] = df['position'].apply(clean_text)

print(df['cleaned_positions'].head())
