# AUTOR: Fabian Calvache
# VALIDACIÓN NOMBRE
while True:
    nombre = input("ingresa tu nombre: ").strip()
    if nombre:
        break
    print("error: el nombre no puede estar vacío")

# VALIDACIÓN APELLIDO PATERNO
while True:
    apellido_paterno = input("ingresa tu apellido paterno: ").strip()
    if apellido_paterno:
        break
    print("error: el apellido paterno no puede estar vacío")

# VALIDACIÓN APELLIDO MATERNO
while True:
    apellido_materno = input("ingresa tu apellido materno: ").strip()
    if apellido_materno:
        break
    print("error: el apellido materno no puede estar vacío")

# VALIDACIÓN EDAD
while True:
    try:
        edad = int(input("ingresa tu edad (ej:22): "))
        break
    except ValueError:
        print("error: debes ingresar un número para la edad")
        # Validación para peso
while True:
    try:
        peso = float(input("ingresa tu peso en kg:(ej.70) "))
        break
    except ValueError:
        print("Error: debes ingresar un número para el peso")

# Validación para altura
while True:
    try:
        altura = float(input("ingresa tu altura en metros:(ej 1.65) "))
        break
    except ValueError:
        print("Error: debes ingresar un número para la altura")

# Cálculo del IMC
imc = peso / (altura ** 2)

# Mostrar resultados
print("\n--- resultado ---")
print(f"nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"edad: {edad} años")
print(f"peso: {peso} kg")
print(f"altura: {altura} m")
print(f"tu índice de masa corporal(IMC) es:{imc:.2f}")
if imc < 18.5:
    clasificacion = 'bajo peso'
elif 18.5 <= imc < 25.0:
    clasificacion = 'peso normal (peso saludable)'
elif 25.0 <= imc < 30.0:
    clasificacion = 'sobrepeso'
else:
    clasificacion = 'obesidad'

# IMPRESION ORDENADA DE LOS DATOS
print('\n' + '=' * 50)
print('resumen del registro y resultados ')
print('=' * 50)
print(f'nombre completo: {nombre} {apellido_paterno} {apellido_materno}')
print(f'edad: {edad} años')
print(f'peso: {peso} kg')
print(f'altura: {altura} m')
print(f'tu indice de masa corporal es (IMC): {imc:.2f}')
print(f'clasificacion : {clasificacion}')
print('=' * 50)
print('gracias por utilizar esta calculadora de IMC ')