import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics
import spacy
import joblib
import numpy as np
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from string import punctuation
from nltk.tokenize import word_tokenize as tokenize  # Add this line

# Download stopwords
nltk.download('stopwords')


# Load the text file
txt_file_path = 'txt/xochitl.txt'  # Replace 'your_file.txt' with the actual path to your text file

with open(txt_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Stopword list to use
spanish_stopwords = stopwords.words('spanish')

# Spanish stemmer
stemmer = SnowballStemmer('spanish')

# Punctuation to remove
non_words = list(punctuation)
non_words.extend(['¿', '¡'])
non_words.extend(map(str, range(10)))

# Cargar el modelo de Spacy para español
nlp = spacy.load('es_core_news_sm')

# Leer el archivo CSV con las columnas 'review_es' y 'sentimiento'
data = pd.read_csv('csv/xochitl_2.csv')
data2 = pd.read_csv('csv/xochitl.csv')

x = np.asanyarray(data2[['dato']])
y = np.asanyarray(data[['predicciones']])

# Dividir el conjunto de datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

# Crear DataFrames para entrenamiento y prueba
train_data = pd.DataFrame({'dato': x_train.flatten(), 'predicciones': y_train.flatten()})
test_data = pd.DataFrame({'dato': x_test.flatten(), 'predicciones': y_test.flatten()})

# Function to preprocess text with SpaCy and NLTK
def preprocess_text(text):
    doc = nlp(text)
    lemmatized_text = ' '.join([token.lemma_ for token in doc if not token.is_punct and not token.is_stop])
    
    # Remove punctuation and tokenize with NLTK
    tokens = word_tokenize(''.join([c for c in text if c not in non_words]))
    stems = [stemmer.stem(item) for item in tokens if item.lower() not in spanish_stopwords]
    nltk_processed_text = ' '.join(stems)

    return lemmatized_text + ' ' + nltk_processed_text

# Apply preprocessing to the training and test sets
train_data['combined_processed_text'] = train_data['dato'].apply(preprocess_text)
test_data['combined_processed_text'] = test_data['dato'].apply(preprocess_text)

# ... (Rest of your existing code)

# Initialize CountVectorizer using NLTK tokenizer
vectorizer = CountVectorizer(
    analyzer='word',
    tokenizer=tokenize,
    lowercase=True,
    stop_words=spanish_stopwords
)

# Tokenize and print the result for each line in the text file
for line in lines:
    result = vectorizer.build_analyzer()(line)
    print(f"Original Text: {line.strip()}")
    print(f"Tokenized Result: {result}")
    print("\n" + "="*50 + "\n")