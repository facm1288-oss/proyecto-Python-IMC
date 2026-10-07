# autor: fabian calvache martinez

nombre = input('ingresa tu nombre: ') #string
apellido_paterno = input('ingresa tu apellido paterno: ') #string
apellido_materno = input('ingresa tu apellido materno: ') #string

# captura de datos en input() y covercion de tipo ( casting )

edad = int(input('ingresa tu edad:(ej. 38) '))
peso = float(input('ingresa tu peso en kg:(ej.70)'))
altura = float(input('ingresa tu altura en metros:(ej 1.65)'))
# calculo del imc
imc = peso / ( altura ** 2 )
# mostrar el resltado del imc 
print (f"\n-- resultado ---")
print(f'nombre completo: ({nombre} {apellido_paterno} {apellido_materno})')
print (f'edad: {edad} años')
print (f'peso: {peso}kg')
print(f'altura: {altura} m')
print(f'tu indice de masa corporal(IMC) es:{imc:.2f}')
print('¡gracias por utilizar esta calcuadora de IMC!')
