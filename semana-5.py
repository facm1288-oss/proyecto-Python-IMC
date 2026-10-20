entrada = input('hola bienvenido por favor ingresa tu edad para validar:')

edad = 0 

if entrada.isnumeric():
    edad = int(entrada)
else:
    print('por favor introduce un numero valido:')
    exit()
    
    if edad <= 0:
        print('OOOOOOOPS,  no puede ser tu edad demasiado joven ')
    elif edad > 100:
        print('OOOOOOOPS,  no puede ser tu edad demasiado anciano')
    elif edad < 18:
        print('ooooooooooops lo siento pero eres menor de edad, NO puedes ingresar')
    else: 
        print('bienvenido a la pagina puedes ingresar')
        
        
        