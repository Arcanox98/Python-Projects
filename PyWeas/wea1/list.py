lista_notas = [20,39,40,50,60,70,20,30,50,54,56]
#              0  1  2  3   4  5
i = 0
sumatoria = 0
rojas , azules =  0 , 0

while i < len(lista_notas):
    sumatoria = sumatoria + lista_notas[i] 
    print(lista_notas[i])
    if lista_notas[i] < 40:
        rojas += 1
    else:
        azules += 1
    i = i + 1
     
promedio= sumatoria / len(lista_notas)


print("promedio",promedio)
print("cantidad de rojos," , rojas )
print("cantidad de azues," , azules )

    