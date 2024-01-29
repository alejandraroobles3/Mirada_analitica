import psycopg2
import pandas as pd

data=pd.read_csv('csv/xochitl.csv')




def agregar_dato(d,p,rs,t,e):
    con=psycopg2.connect(database="mirada.analitica", user="postgres",
    password="Ale123roblesmora",host="localhost")
    cursor1=con.cursor()

    dato=[d,p,rs,t,e]

    cursor1.execute("insert into analisis.dato (dato,id_prediccion,id_estado,id_red_social,id_tema,id_candidato) values (%s,%s,%s,%s,%s) ",dato)
    con.commit()
    cursor1.close()
    con.close()

print(data['dato'][1])

dato=[]
prediccion=[]

dato=data['dato']
prediccion=data['predicciones']
red_social=1


print(prediccion)