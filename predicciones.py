import joblib
import spacy
import psycopg2

nlp= spacy.load('es_core_news_sm')

clf=joblib.load('entrenamiento/modelo_entrenado.pkl')

def preprocess_text(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc if not token.is_punct and not token.is_stop])


new_text = ""
preprocessed_new_text = preprocess_text(new_text)

prediction= clf.predict([preprocessed_new_text])[0]
print(f'Clasificación del nuevo texto: {prediction}')


def agregar_dato(d,p,rs,t,e):
    con=psycopg2.connect(database="mirada_analitica", user="postgres",
    password="Ale123roblesmora",host="localhost")
    cursor1=con.cursor()

    dato=[d,p,rs,t,e]

    cursor1.execute("insert into analisis.dato (dato,id_prediccion,id_red_social,id_tema,id_eleccion) values (%s,%s,%s,%s,%s) ",dato)
    con.commit()
    cursor1.close()
    con.close()