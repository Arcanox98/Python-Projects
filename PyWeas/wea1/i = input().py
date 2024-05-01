peso = int(input("Ingrese su peso"))
altura = float(input("Ingrese su altura"))
imc = (peso)/(altura*altura)
print(imc)
if imc < 18.5:
    print("bajo")
elif imc >= 18.5 and imc > 25:
    print("normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
else:
    print("obeso") 