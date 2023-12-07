'string' 
"string"
""""string 
en varias lineas"""

3 
4.2 

False 

numero = 10
numero += 5
name  = 'Franco'
del name #elimina un dato
name = 'Fran'
print('fr' in name) #Booleano que indica si los caracteres se encuentran en la variable
print('fr' not in name)
print (f"hola {numero}") #fstring: Toma un dato y lo convierte a texto
lista = [1, 2, 3, 'hola']
tupla = (1,2,3) #No se pueden modificar
print(lista)
conjunto = {1,2,3,4} #No se pueden acceder a elementos por el indice y no almacena datos duplicados.
diccionario = {
    'nombre': 'franco',
    'apellido': 'serafini',
    'edad': 25
}
print(diccionario['nombre'])
print(type(name))