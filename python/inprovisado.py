import pandas as pd

data = pd.read_csv('csv/xochitl_2.csv')

x = data['dato']

with open('txt/udg.txt', 'w', encoding='utf-8') as f:
    for item in x:
        f.write("%s\n" % item)




"""def agregar_dato(d,p,rs,t,e):
    con=psycopg2.connect(database="mirada_analitica", user="postgres",
    password="Ale123roblesmora",host="localhost")
    cursor1=con.cursor()

    dato=[d,p,rs,t,e]

    cursor1.execute("insert into analisis.dato (dato,id_prediccion,id_red_social,id_tema,id_eleccion) values (%s,%s,%s,%s,%s) ",dato)
    con.commit()
    cursor1.close()
    con.close()"""