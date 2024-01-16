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

# Preprocesamiento de texto con SpaCy (lemmatization, deeper tokenization)
def preprocess_text(text):
    # Tokenization and Lemmatization with SpaCy
    doc = nlp(text)
    lemmatized_text = ' '.join([token.lemma_ for token in doc if not token.is_punct and not token.is_stop])



# Aplicar preprocesamiento a los conjuntos de entrenamiento y prueba
train_data['processed_text'] = train_data['dato'].apply(preprocess_text)
test_data['processed_text'] = test_data['dato'].apply(preprocess_text)

# Crear un clasificador con un modelo de bolsa de palabras y Naive Bayes
model = joblib.load('modelo_entrenado2.pkl')

# Entrenar el modelo con los datos de entrenamiento
model.fit(train_data['processed_text'], train_data['predicciones'])

# Predecir el conjunto de prueba
predicted_sentiments = model.predict(test_data['processed_text'])

# Medir la precisión del modelo
accuracy = metrics.accuracy_score(test_data['predicciones'], predicted_sentiments)
print(f'Precisión del modelo: {accuracy:.2f}')

# Imprimir ejemplos de predicciones en el conjunto de prueba
print("\nEjemplos de predicciones en el conjunto de prueba:")
for i in range(5):
    print(f'Texto: {test_data["dato"].iloc[i]}')
    print(f'Predicción: {predicted_sentiments[i]}')
    print(f'Etiqueta real: {test_data["predicciones"].iloc[i]}\n')

# Clasificar un nuevo texto
new_text = "Este producto es exelente, lo recomiendoo totalmentee."
preprocessed_new_text = preprocess_text(new_text)
prediction = model.predict([preprocessed_new_text])[0]
print(f'Clasificación del nuevo texto: {prediction}')
   



"""def agregar_dato(d,p,rs,t,e):
    con=psycopg2.connect(database="mirada_analitica", user="postgres",
    password="Ale123roblesmora",host="localhost")
    cursor1=con.cursor()

    dato=[d,p,rs,t,e]

    cursor1.execute("insert into analisis.dato (dato,id_prediccion,id_red_social,id_tema,id_eleccion) values (%s,%s,%s,%s,%s) ",dato)
    con.commit()
    cursor1.close()
    con.close()"""