entrada = input('hola bienvenido por favor ingresa tu edad para validar:')
# Entrega parcial de la semana 5 en Python 

edad = 0 
def evaluar_palabra():
    """Función 1: Compara la longitud de un string usando len() y estructuras if-elif-else."""
    palabra = input("Ingresa una palabra: ")
    longitud = len(palabra)
    print(f"La palabra ingresada tiene {longitud} letras.")

if entrada.isnumeric():
    edad = int(entrada)
else:
    print('por favor introduce un numero valido:')
    exit()
    if 4 <= longitud <= 8:
        print("Palabra correcta (tiene entre 4 y 8 letras).")
    elif longitud < 4:
        print("Hacen falta letras (tiene menos de 4 letras).")
    else:
        print("Demasiadas letras (tiene más de 8 letras).")
def evaluar_cuadrante():
    """Función 2: Evalúa si X y Y son positivos o negativos para determinar el cuadrante."""
    try:
        x = float(input("Ingresa el valor de X: "))
        y = float(input("Ingresa el valor de Y: "))
    except ValueError:
        print("Error: Debes ingresar valores numéricos válidos.")
        return

    if x > 0 and y > 0:
        print(f"El punto ({x}, {y}) pertenece al Cuadrante I.")
    elif x < 0 and y > 0:
        print(f"El punto ({x}, {y}) pertenece al Cuadrante II.")
    elif x < 0 and y < 0:
        print(f"El punto ({x}, {y}) pertenece al Cuadrante III.")
    elif x > 0 and y < 0:
        print(f"El punto ({x}, {y}) pertenece al Cuadrante IV.")
    else:
        print("El punto se encuentra sobre uno de los ejes coordenados (X=0 o Y=0).")


# Ejecución principal del programa
if __name__ == "__main__":
    print("=== PARTE 1: VALIDACIÓN DE PALABRA ===")
    evaluar_palabra()
    
    if edad <= 0:
        print('OOOOOOOPS,  no puede ser tu edad demasiado joven ')
    elif edad > 100:
        print('OOOOOOOPS,  no puede ser tu edad demasiado anciano')
    elif edad < 18:
        print('ooooooooooops lo siento pero eres menor de edad, NO puedes ingresar')
    else: 
        print('bienvenido a la pagina puedes ingresar')
        
    print("\n=== PARTE 2: PLANO CARTESIANO (CUADRANTES) ===")
    evaluar_cuadrante()
        
        