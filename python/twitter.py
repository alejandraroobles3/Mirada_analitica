import joblib
import spacy
import psycopg2
import codecs
import csv

# Abre el archivo en modo lectura
with codecs.open('txt/xochitl.txt', 'r', 'UTF-8') as f:
    # Itera sobre cada línea en el archivo
    lines=[]
    for line in f:
        new=line.strip('\n')
        new=new.strip('\r')
        lines.append(str(new))

with codecs.open('txt/pred.txt', 'r', 'UTF-8') as f:
    # Itera sobre cada línea en el archivo
    lines2=[]
    for line in f:
        new=line.strip('\n')
        new=new.strip('\r')
        lines2.append(str(new))





with open('csv/xochitl.csv', 'w', encoding='UTF-8',newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['dato','predicciones'])
    for l in range(0,len(lines)):
        writer.writerow([lines[l],lines2[l]])