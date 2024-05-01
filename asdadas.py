def is_palindrome(palabra):
    # TODO: completar funcion
    lista = palabra

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
    return palindrome
palabra_test = "ana"
if is_palindrome(palabra_test) == True:
    print("👍palabra palindrome")
else:
    print("❌palabra no es palindorme")
