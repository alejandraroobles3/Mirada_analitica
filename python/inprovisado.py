import codecs

# Abre el archivo en modo lectura
with codecs.open('txt/claudia.txt', 'r', 'UTF-8') as f:
    # Itera sobre cada línea en el archivo
    lines=[]
    for line in f:
        lines.append(line)
        
print(lines[0])


def agregar_dato(d,p,rs,t,e):
    con=psycopg2.connect(database="mirada_analitica", user="postgres",
    password="Ale123roblesmora",host="localhost")
    cursor1=con.cursor()

    dato=[d,p,rs,t,e]

    cursor1.execute("insert into analisis.dato (dato,id_prediccion,id_red_social,id_tema,id_eleccion) values (%s,%s,%s,%s,%s) ",dato)
    con.commit()
    cursor1.close()
    con.close()