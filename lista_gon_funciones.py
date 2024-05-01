def determinar_numero_existe(lista : list[int] , numero_a_comprobar : int ) -> bool :
    i = 0
    existe = False
    while i < len(lista):
        if lista[i] == numero_a_comprobar:
            existe = True
            break
        i += 1
    return existe

def mostrar_cliente_existe_numero(lista : list, numero: int) -> None:
    if determinar_numero_existe(lista, numero) :
        print("Existe un",numero)
    else:
        print("No existe",numero)


# aqui parte programa 

lista_gon = [1,2,2,5,4,10]
numeros_a_comprobar = [3,5,10,34]
for numero in numeros_a_comprobar:
    mostrar_cliente_existe_numero(lista_gon ,numero)


