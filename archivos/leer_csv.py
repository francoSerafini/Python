import csv

with open("archivos\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:  #Bucle para leer las lineas.
        print(row)