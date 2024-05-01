numero = int(input("Ingrese numero"))
a = object(2)
i = 2
is_primo = True
while i < numero :
    eval = numero % i
    if eval == 0:
        is_primo = False
        break
    i =  i + 1
     

if is_primo:
    print("El numero es primo")
else:
    print("El numero no es primo")


# numero = 5
# for i in range(2,numero):
#     print(i)