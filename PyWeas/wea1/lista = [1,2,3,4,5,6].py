lista = [1,2,3,4,4,6]
lenght = len(lista)
i = 0
existe3 = False
existe5 = False
existe10 = False


while i < lenght:
    recorrer = lista[i]
    if recorrer == 3:
        existe3 = True
    if recorrer == 5:
        existe5 = True
    if recorrer == 10:
        existe10 = True
    i+= 1
if existe3 == True:
    print("numero 3 Si")
else:
    print("Numero 3 no")
if existe5 == True:
    print("numero 5 Si")
else:
    print("Numero 5 no")
if existe10 == True:
    print("numero 10 Si")
else:
    print("Numero 10 no")