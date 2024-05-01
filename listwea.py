lista_ordenada = [1,2,3,4,5,6,7,8,9]
i = 0
lenghtPrimario = len(lista_ordenada)
print(lista_ordenada)
while i < len(lista_ordenada):

    if lista_ordenada[i] != lista_ordenada[i+1]:
        lenght = 11 - i 
        lista_ordenada.append(lenght - 1)
    elif lista_ordenada[8] == 9:
        del lista_ordenada[:9]
        break
    i += 1
print(lista_ordenada)