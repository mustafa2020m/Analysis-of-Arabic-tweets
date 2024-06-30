#import all necessary packages
from nltk.corpus import stopwords
import re, pickle, numpy as np
import warnings
warnings.simplefilter('ignore')

def preprocess_arabic_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove special characters and numbers
    text = re.sub(r'[^ء-ي\s]', ' ', text)  # Adjust the range based on your specific needs
    # Remove emojis and non-word characters
    text = re.sub(r'[^\w\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove Twitter handles
    text = re.sub(r'@[^\s]+', '', text)
    # Remove hashtags
    text = re.sub(r'\B#\S+', '', text)
    # Remove single characters
    text = re.sub(r'\s+[a-zA-Z]\s+', '', text)
    # Substituting multiple spaces with single space
    text = re.sub(r'\s+', ' ', text, flags=re.I)
    # Tokenization
    words = text.split()
    # Remove stopwords
    stop_words = set(stopwords.words('arabic'))
    words = [word for word in words if word not in stop_words]
    # Join the words back into a string
    processed_text = ' '.join(words)
    return processed_text




