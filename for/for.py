lista = ['a','b','c']

for vocal in lista:
    print(f'Esto es una vocal: {vocal}')
    
nombre = 'hola me llamo franco'

for letra in nombre:
    print(letra)
    
#Recorrer dos listas (recorre la cantidad de veces menor)

for vocal,letra in zip(lista,nombre):
    print('vocal: ', vocal)
    print('letra: ', letra)
    
    
for letra in enumerate(nombre):
    print(letra)
    
persona = {
    'nombre': 'Franco',
    'apellido':'Serafini',
    'edad': 25
}

for dato in persona.values():
    print(dato)
    
for dato in persona:
    print(dato)
    
for dato in persona.items():
    print(dato)