frase = input('ingrese una frase: ')
cantidad_palabras = len(frase.split(' '))

resultado = (cantidad_palabras / 2)

print(f'Tardarias en decir esa frase {resultado} segundos')
print(f'Dijiste {cantidad_palabras}')
print(f'A un 30% mas de velociadad tardarias {resultado - (resultado * 0.30)}')

if(resultado > 120):
    print('Dijiste una frase muy larga')
