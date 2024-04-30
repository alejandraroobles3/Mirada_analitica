import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics
import spacy
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.svm import LinearSVC

# Cargar el modelo de Spacy para español
nlp = spacy.load('es_core_news_sm')

# Leer el archivo CSV
data = pd.read_csv('entrenamiento/IMDB Dataset SPANISH.csv')

# Dividir el conjunto de datos
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Función de preprocesamiento
def preprocess_text(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc if not token.is_punct and not token.is_stop])

# Aplicar preprocesamiento
train_data['processed_text'] = train_data['review_es'].apply(preprocess_text)
test_data['processed_text'] = test_data['review_es'].apply(preprocess_text)

# Clasificador Naive Bayes
model = make_pipeline(CountVectorizer(), LinearSVC())
model.fit(train_data['processed_text'], train_data['sentimiento'])
predicted_sentiments = model.predict(test_data['processed_text'])

# Precisión del modelo
accuracy = metrics.accuracy_score(test_data['sentimiento'], predicted_sentiments)
print(f'Precisión del modelo: {accuracy:.2f}')

# Comparación de predicciones y etiquetas reales
results = pd.DataFrame({'Reales': test_data['sentimiento'], 'Predicciones': predicted_sentiments})
comparison = pd.crosstab(results['Reales'], results['Predicciones'])

# Gráfico de comparación
plt.figure(figsize=(10, 5))
sns.heatmap(comparison, annot=True, fmt='d', cmap='Blues')
plt.title('Comparación de etiquetas reales vs. predicciones')
plt.ylabel('Etiqueta Real')
plt.xlabel('Predicción')
plt.show()

# Matriz de confusión
cm = confusion_matrix(test_data['sentimiento'], predicted_sentiments)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap='viridis')
plt.title('Matriz de Confusión')
plt.show()