import psycopg2
import pandas as pd

#20,089 sin



data=pd.read_csv('csv/jorge.csv')
def pred(prediccion):
    
    id=[]
    for i in prediccion:
        if i == 'positivo':
            id.append(1)
        else: 
            id.append(2)
    
    return id

con=psycopg2.connect(database="mirada_analitica", user="administrador", password="Ale123roblesmora",host="mirada.postgres.database.azure.com", port="5432")
cursor1=con.cursor()

def agregar_dato(dat,pred,estado,rs,tem,cand):
    dato=[dat,pred,estado,rs,tem,cand]

    cursor1.execute("insert into dato (dato,id_prediccion,id_estado,id_red_social,id_tema,id_candidato) values (%s,%s,%s,%s,%s,%s) ",dato)
    con.commit()



dato=[]
prediccion=[]

dato=data['dato']
prediccion=data['predicciones']
red_social=1
candidato=3
estado=33
tema=1
id=[]

id=pred(prediccion)

print(len(id), len(dato))

for i in range(1,len(dato)): #len(dato)
    d=dato[i]
    p=id[i]
    agregar_dato(d,p,estado,red_social,tema,candidato)

cursor1.close()
con.close()
