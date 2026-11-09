pila = [5, 10, 15, 20, 25]
while len(pila) >= 3:
    if pila[-1] % 3 == 0:
        extraido = pila.pop()
        pila.append(extraido + 1)
        print(pila )
        
    else:
        print("todos los elementos de pila son multiplos de 3")
        break

    