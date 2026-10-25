print('---programa de variantes---')
x = 0
y = 0
# Validar coordenada x (no puede ser o)
while x == 0:
    x=float(input('ingresa coordenada x (diferente de 0):'))
    if x == 0:
        print('¡Error! la coordenada x no ser cero. Intentalo de nuevo.')

# Validar coordenada y ( no puede ser 0)
while y == 0:
    y=float( input('ingrsa coordenada y (diferente de 0):'))
    if y == 0:
        print('¡Error! la coordenada y no puede ser cero. Intentalo de nuevo.')
        
# Determinar el cuadrante correspondiente.
if x>0 and y>0:
    print(f'el punto({x},{y})se encuentra en *el primer cuadrante*.') 
elif x<0 and y>0:
    print(f'El punto({x},{y})se encuentra en el *segundo caudrante*.')
elif x<0 and y<0:
    print(f'El punto({x},{y})se encuentra en el *tercer cuadrante*.')
else:
    print(f'El punto ({x},{y})se encuentra en el *cuarto cuadrante*.')
    
print('\ n ====PROGRAMA DE LONGITUD DE AREA\PALABRA===')
palabra_secreta='usuario'
# Ciclo while que se repite si la palabra es incorrecta
palabra_usuario = input('Ingresa la palabra secreta: ')
while palabra_usuario.lower() != palabra_secreta:
    print('Palabra incorrecta. Inténtalo de nuevo.')
    palabra_usuario = input('Ingresa la palabra secreta: ')
print('¡Palabra correcta!')
    