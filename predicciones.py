import joblib
import spacy
import psycopg2
import codecs
import csv

nlp= spacy.load('es_core_news_sm')

clf=joblib.load('entrenamiento/modelo_entrenado.pkl')

# Abre el archivo en modo lectura
with codecs.open('txt/xochitl.txt', 'r', 'UTF-8') as f:
    # Itera sobre cada línea en el archivo
    lines=[]
    for line in f:
        new=line.strip('\n')
        new=new.strip('\r')
        lines.append(str(new))


def preprocess_text(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc if not token.is_punct and not token.is_stop])

predicciones=[]

for l in lines:
    new_text = l
    preprocessed_new_text = preprocess_text(new_text)
    
    prediction= clf.predict([preprocessed_new_text])[0]
    #print(f'Clasificación del nuevo texto: {prediction}',lines[l])
    predicciones.append(str(prediction))


with open('csv/xochitl.csv', 'w', encoding='UTF-8',newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(["'"+'dato'+"'","'"+'predicciones'+"'"])
    for l in range(0,len(lines)):
        writer.writerow(["'"+lines[l]+"'","'"+predicciones[l]+"'"])




