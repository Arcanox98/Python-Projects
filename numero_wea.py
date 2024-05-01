import math

def numero_wea(numero):
    if numero < 0:
        numeroPositivo = numero * -1
        numeroTruncado = math.trunc(numeroPositivo)
        respuestaNumero = numeroPositivo - numeroTruncado
        transToStr = str(numeroPositivo)
        toStrList = transToStr.split(".")
        lenght = len(toStrList[1])
        return round(respuestaNumero, lenght)
    else:
        numeroTruncado= math.trunc(numero)
        respuestaNumero = numero - numeroTruncado
        transToStr = str(numero)
        toStrList = transToStr.split(".")
        lenght = len(toStrList[1])
        return round(respuestaNumero, lenght)

