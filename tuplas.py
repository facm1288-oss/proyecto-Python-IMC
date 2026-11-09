#son una coleccion inmutable es un acoleccion de elmentos que ya no peodemos modificar una vez definidos 
vocales = ('a', 'e', 'i', 'o', 'u')
print(vocales[2])
print(vocales[:3]+vocales[2:])
print(vocales.index('o'))
lista_vocales= list(vocales)
lista_vocales[2]='I'
print(lista_vocales)
tupla_vocales = tuple(lista_vocales)
lista_vocales[2]='I'
print(lista_vocales)
print(tupla_vocales)    
