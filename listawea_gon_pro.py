lista = [1,2,3,4,5,6,7,8]

j = len(lista) - 1
i = 0
print(lista)
while i < j:
    aux = lista[j]
    lista[j] = lista[i]
    lista[i] = aux

    i += 1
    j -= 1

print(lista)