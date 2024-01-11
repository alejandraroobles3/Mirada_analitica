import joblib
import spacy
import psycopg2
import codecs

nlp= spacy.load('es_core_news_sm')

clf=joblib.load('entrenamiento/modelo_entrenado.pkl')

# Abre el archivo en modo lectura
with codecs.open('txt/claudia.txt', 'r', 'UTF-8') as f:
    # Itera sobre cada línea en el archivo
    lines=[]
    for line in f:
        lines.append(line)

def preprocess_text(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc if not token.is_punct and not token.is_stop])


for l in range(0,200):
    new_text = lines[l]
    preprocessed_new_text = preprocess_text(new_text)
    
    prediction= clf.predict([preprocessed_new_text])[0]
    print(f'Clasificación del nuevo texto: {prediction}',lines[l])




