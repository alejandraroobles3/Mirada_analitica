import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import spacy
import joblib
from sklearn.neural_network import MLPClassifier

# Cargar el modelo de Spacy 
nlp = spacy.load('es_core_news_sm')

# Leer el archivo CSV 
data = pd.read_csv('csv/xochitl.csv')

# Dividir el conjunto de datos en entrenamiento y prueba
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Preprocesamiento de texto con Spacy
def preprocess_text(text):
    
    doc = nlp(text)
    return ' '.join([token.lemma_.lower() for token in doc if not token.is_punct and not token.is_stop])

# Aplicar preprocesamiento a los conjuntos de entrenamiento y prueba
train_data['processed_text'] = train_data['dato'].apply(preprocess_text)
test_data['processed_text'] = test_data['dato'].apply(preprocess_text)

#clasificador 
model = make_pipeline(CountVectorizer(), MLPClassifier())

# Entrenar el modelo con los datos de entrenamiento
model.fit(train_data['processed_text'], train_data['predicciones'])

# Predecir el conjunto de prueba
predicted_sentiments = model.predict(test_data['processed_text'])

# Medir la precisión del modelo
accuracy = metrics.accuracy_score(test_data['predicciones'], predicted_sentiments)
print(f'Precisión del modelo: {accuracy:.2f}')

# Imprimir ejemplos de predicciones
print("\nEjemplos de predicciones en el conjunto de prueba:")
for i in range(5):
    print(f'Texto: {test_data["processed_text"].iloc[i]}')
    print(f'Predicción: {predicted_sentiments[i]}')
    print(f'Etiqueta real: {test_data["predicciones"].iloc[i]}\n')

# Clasificar un nuevo texto
new_text = "Este producto es excelente, lo recomiendo totalmente."
preprocessed_new_text = preprocess_text(new_text)
prediction = model.predict([preprocessed_new_text])[0]
print(f'Clasificación del nuevo texto: {prediction}')

import joblib

#joblib.dump(model, 'entrenamiento/modelo_entrenado2.pkl')