lista = "arriba"

i = 0
j = len(lista) - 1
palindrome = False
while i < j:
    if lista[j] == lista [i]:
        palindrome = True
    elif lista[j] != lista[i]:
          palindrome = False
    i += 1
    j -= 1
if palindrome == True:
     print("palabra palindrome")
else:
     print("palabra no es palindrome")