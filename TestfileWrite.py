def writeOnFile(str):
    file = open("tarea", "w")
    escribir = str(input("Ingrese notas separadas por,: "))
    file.write(str(escribir))
    file.close()
    return str(escribir)

