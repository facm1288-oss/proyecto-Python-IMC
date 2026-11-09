# Reto semana 7 optimizacion con colecciones

# TUPLA 1. almacena los nombres fijos de los cuadarantes.
# Las tuplas son inmutables(los valores no cambian durante la ejecucion)
# Se accede a ellos mediante indices numericos (0,1,2,3)
cuadrantes = ('Cuadrante 1', 'Cuadrante 2', 'Cuadrante 3', 'Cuadrante 4')

# 2 LISTA. Almacena de forma dinamica las plabras o regitros ingresados por el usuario
# las listas son mutables lo que permite agregar elemntos usando append() o eliminar elementos con remove()
historial_palabras = []
print('GESTOR DE REGISTRO POR CUADRANTES')
print(f'cuadrantes disponibles: {cuadrantes [0]}, {cuadrantes [1]}, {cuadrantes [2]}, {cuadrantes [3]}\n')

# BUCLE PRINCIPAL PARA LA INTERACCION CON EL USUARIO.
while True:
    # solicitamos el ingreso de una palabra o registro
    palabra_ingresada = input('Ingrese una palabra o registro (o escriba "salir" para terminar): ').strip()
    # condicion de salida del bucle
    if palabra_ingresada.lower() == 'salir':
        print('\n Saliendo del programa...')
        break
    # validamos que el usario  no deje campos vacios 
    if not palabra_ingresada:
        print('Error: No se puede ingresar un campo vacio. Intente nuevamente.\n')
        continue
    # Agregamos la palabra ingresada a nuestra LISTA (historial)
    historial_palabras.append(palabra_ingresada)

    # Ejemplo de uso de la tupla mediante indices para clasificar o demostrar informacion.
    # Simulamos la asiganccion al primer cuadrante por defecto segun la logica del programa
    print(f'registro guardado exitosamente en cuadrante: {cuadrantes[0]}')
    print(f'Total de las palabras registradas hasta el momento: {len(historial_palabras)}\n')

    # REPORTE FINAL DE LA SESIÓN
    print('\n' + '+' + '=' * 40)
    print('REPORTE FINAL DE LA SESIÓN')
    print(f'Total de palabras ingresadas: {len(historial_palabras)}')
    # Mostramos el contenido final  de la lista acumulada
    if historial_palabras:
        print('historial completo de palabras ingresadas:')
        for i, palabra in enumerate(historial_palabras, start=1):
            print(f'{i}. {palabra}')
        else:
            print('No se ingresaron palabras durante la sesión.')
            print('='*40)
            print('reto completado con exito')