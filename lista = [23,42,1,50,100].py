def numero_mayor (lista):
    i = 0
    print(lista)
    mayor = float("-inf")
    while i < len(lista):
        if lista[i] > mayor:
            mayor = lista[i]
        i+= 1
        
    return mayor
lista_benja = [4,42,15,2]
print(numero_mayor(lista_benja))