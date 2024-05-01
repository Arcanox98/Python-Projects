lista = [1,2,3,4,5,6,7,8,100]
#                         ^
#                         i
lista_alrevez = []

i = len(lista) - 1
while i >= 0:
    lista_alrevez.append(lista[i])
    i -= 1


print(lista_alrevez)
