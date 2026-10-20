# AUTOR: Fabian Calvache
# VALIDACIÓN NOMBRE
# while True:
#     nombre = input("ingresa tu nombre: ").strip()
#     if nombre:
#         break
#     print("error: el nombre no puede estar vacío")

# # VALIDACIÓN APELLIDO PATERNO
# while True:
#     apellido_paterno = input("ingresa tu apellido paterno: ").strip()
#     if apellido_paterno:
#         break
#     print("error: el apellido paterno no puede estar vacío")

# # VALIDACIÓN APELLIDO MATERNO
# while True:
#     apellido_materno = input("ingresa tu apellido materno: ").strip()
#     if apellido_materno:
#         break
#     print("error: el apellido materno no puede estar vacío")

# # VALIDACIÓN EDAD
# while True:
#     try:
#         edad = int(input("ingresa tu edad (ej:22): "))
#         break
#     except ValueError:
#         print("error: debes ingresar un número para la edad")
#         # Validación para peso
# while True:
#     try:
#         peso = float(input("ingresa tu peso en kg:(ej.70) "))
#         break
#     except ValueError:
#         print("Error: debes ingresar un número para el peso")

# # Validación para altura
# while True:
#     try:
#         altura = float(input("ingresa tu altura en metros:(ej 1.65) "))
#         break
#     except ValueError:
#         print("Error: debes ingresar un número para la altura")

# # Cálculo del IMC
# imc = peso / (altura ** 2)

# # Mostrar resultados
# print("\n--- resultado ---")
# print(f"nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
# print(f"edad: {edad} años")
# print(f"peso: {peso} kg")
# print(f"altura: {altura} m")
# print(f"tu índice de masa corporal(IMC) es:{imc:.2f}")
# if imc < 18.5:
#     clasificacion = 'bajo peso'
# elif 18.5 <= imc < 25.0:
#     clasificacion = 'peso normal (peso saludable)'
# elif 25.0 <= imc < 30.0:
#     clasificacion = 'sobrepeso'
# else:
#     clasificacion = 'obesidad'

# # IMPRESION ORDENADA DE LOS DATOS
# print('\n' + '=' * 50)
# print('resumen del registro y resultados ')
# print('=' * 50)
# print(f'nombre completo: {nombre} {apellido_paterno} {apellido_materno}')
# print(f'edad: {edad} años')
# print(f'peso: {peso} kg')
# print(f'altura: {altura} m')
# print(f'tu indice de masa corporal es (IMC): {imc:.2f}')
# print(f'clasificacion : {clasificacion}')
# print('=' * 50)
# print('gracias por utilizar esta calculadora de IMC ')

# =========================================================
# Proyecto: Calculadora de Índice de Masa Corporal (IMC)
# Descripción: Captura datos personales y métricos del usuario,
#              aplica validaciones robustas y muestra el IMC formateado.
# =========================================================

# --- Captura y formateo de nombres 2da entrega final
nombre = input("Ingresa tu nombre: ").strip()
apellido_paterno = input("Ingresa tu apellido paterno: ").strip()
apellido_materno = input("Ingresa tu apellido materno: ").strip()

# Validar que los campos de texto no estén vacíos
while not nombre or not apellido_paterno or not apellido_materno:
    print("[Error] Los campos de nombre y apellidos no pueden estar vacíos.")
    nombre = input("Ingresa tu nombre: ").strip()
    apellido_paterno = input("Ingresa tu apellido paterno: ").strip()
    apellido_materno = input("Ingresa tu apellido materno: ").strip()

# Formatear el nombre completo con mayúsculas iniciales (.title())
nombre_completo = f"{nombre.title()} {apellido_paterno.title()} {apellido_materno.title()}"


# --- Función auxiliar para validar datos numéricos y mayores a cero ---
def solicitar_numero(mensaje, es_entero=False):
    while True:
        valor_str = input(mensaje).strip()
        if not valor_str:
            print("[Error] El campo no puede estar vacío.")
            continue
        try:
            if es_entero:
                valor = int(valor_str)
            else:
                valor = float(valor_str)
            
            # Validación sugerida: asegurar que sea mayor a cero
            if valor <= 0:
                print("[Error] El valor ingresado debe ser mayor a cero.")
                continue
            return valor
        except ValueError:
            print("[Error] Entrada inválida. Ingresa solo cifras numéricas.")


# Captura validada de edad, peso y estatura
edad = solicitar_numero("Ingresa tu edad: ", es_entero=True)
peso = solicitar_numero("Ingresa tu peso en kg (ejemplo: 70.5): ")
altura = solicitar_numero("Ingresa tu altura en metros (ejemplo: 1.65): ")


# --- Cálculo del IMC ---
imc = peso / (altura ** 2)


# --- Clasificación del IMC (Rangos sin huecos) ---
if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 25:
    clasificacion = "Peso normal (Saludable)"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"


# --- Única impresión del reporte final (sin duplicados) ---
print("\n" + "=" * 45)
print("         RESUMEN DE DATOS Y RESULTADO        ")
print("=" * 45)
print(f"Nombre completo: {nombre_completo}")
print(f"Edad:            {edad} años")
print(f"Peso:            {peso} kg")
print(f"Estatura:        {altura} m")
print(f"IMC:             {imc:.2f}")
print(f"Clasificación:   {clasificacion}")
print("=" * 45)