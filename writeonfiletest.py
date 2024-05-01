def writeOnFile(str):
    file = open("tarea", "w")
    escribir = str(input("Ingrese notas separadas por,: "))
    file.write(str(escribir))
    file.close()
    return str(escribir)
def readOnFile():
    file = open("tarea", "r")
    content  = file.read()
    suma = 0
    i = 0
    notas = content.split(",")

    lenght = len(notas)
    while i < lenght:
        suma += int(notas[i])
        i += 1
    promedio = suma / lenght
    print(promedio) 
    file.close()
    return round(promedio)

