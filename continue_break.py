# uso de la sentencia continue en un ciclo for 
# for numero in range(1, 11):
#     if numero % 2 == 1:
#         continue
#     print(f'(numero el numero es par: {numero}')
    
# sentencia continue con el ciclo while
# numero = 0
# while numero < 11:
#     numero += 1
#     if numero % 2 == 0:
#         continue
#     print(f' elnumero es impar: {numero}')
# uso de la sentencia break
# class buscado:
#     def __init__(self, numero, limite_inferior=0, limite_superior=10):
#         self.numero = numero
#         self.limite_inferior = limite_inferior
#         self.limite_superior = limite_superior

#     def buscar(self):
#         intentos = 0
#         while self.limite_inferior <= self.limite_superior:
#             intentos += 1
#             intento = (self.limite_inferior + self.limite_superior) // 2
#             if intento == self.numero:
#                 print(
#                     f'Felicidades, el numero {self.numero} fue encontrado '
#                     f'en {intentos} intentos'
#                 )
#                 return intento
#             if intento < self.numero:
#                 self.limite_inferior = intento + 1
#             else:
#                 self.limite_superior = intento - 1

#         print('El numero no se encuentra dentro del rango.')
#         return None


# if __name__ == '__main__':
#     numero = int(input('Ingrese un digito (0-10): '))
#     buscado(numero).buscar()
#     print('fin del programa')
    
 
#==================================================================
# Uso de la funcion exit() para salir de un programa
# class buscado:
#     def __init__(self, numero, limite_inferior=0, limite_superior=10):
#         self.numero = numero
#         self.limite_inferior = limite_inferior
#         self.limite_superior = limite_superior

#     def buscar(self):
#         intentos = 0
#         while self.limite_inferior <= self.limite_superior:
#             intentos += 1
#             intento = (self.limite_inferior + self.limite_superior) // 2
#             if intento == self.numero:
#                 print(f'Felicidades, el numero {self.numero} fue encontrado '
#                       f'en {intentos} intentos')      
#                 return intento
#             if intento < self.numero:
#                 self.limite_inferior = intento + 1
#             else:
#                 self.limite_superior = intento - 1

#         print('El numero no se encuentra dentro del rango.')
#         return None


# if __name__ == '__main__':
#     numero = int(input('Ingrese un digito (0-10): '))
#     buscado(numero).buscar()
#     print('fin del programa')
# numero=int(input('Ingrese un digito : '))
# limitie_inferior=0
# limitie_superior=10
# buscado=5
# intentos=0

# while True:
#     intentos+=1
#     if numero == buscado:
        
        
#         print(f'Felicidades, el numero {numero} fue encontrado en {intentos} intentos')
#         break
#     elif numero < buscado:
#         limite_superior = buscado
#         buscado = ( buscado + limitie_inferior ) // 2
#     else:
#         limite_inferior = buscado
#         buscado = ( buscado + limitie_superior ) // 2
# exit()
# print('FIN DEL PROGRAMA')

intentos = 0
while True:
    intentos += 1
    print(f'Intento: {intentos}')
    if intentos == 20:
        print('fin del programa')
        exit()
        
        print('Este mensaje no se mostrará porque el programa ha salido')
    
    