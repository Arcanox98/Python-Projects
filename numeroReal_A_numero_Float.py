import math
import discord
import numero_wea

bot = discord.Client()

numero = float(input("Ingrese numero flotante: "))

#TODO: ningun linea repetida, principio DRY

if numero < 0:
    numeroPositivo = numero * -1
    numeroTruncado = math.trunc(numeroPositivo)
    respuestaNumero = numeroPositivo - numeroTruncado
    transToStr = str(numeroPositivo)
    toStrList = transToStr.split(".")
    lenght = len(toStrList[1])
    respuestaNumeroRedondeado = round(respuestaNumero, lenght)
    print(respuestaNumeroRedondeado)
else:
    numeroTruncado= math.trunc(numero)
    respuestaNumero = numero - numeroTruncado
    transToStr = str(numero)
    toStrList = transToStr.split(".")
    lenght = len(toStrList[1])
    respuestaNumeroRedondeado = round(respuestaNumero, lenght)
    print(respuestaNumeroRedondeado)

