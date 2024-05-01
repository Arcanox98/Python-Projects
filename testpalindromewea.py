lista_test = [ ("reconocer",True) ,("anilina",True) ,
            ("none",False) , ("poto",False) , ("arriba",True) ,("ana", True) ,
            ("caca",False) , ("level" ,True) ]
lista = lista_test
i = 0
j = len(lista) - 1
palindrome = False
while i < j:

    if lista[j] == lista [i]:
        print("1",lista[i],"2",lista[j])
        palindrome = True
    elif lista[j] != lista[i]:
        palindrome = False
    i += 1
    j -= 1
if palindrome == True:
    print("Palabra es palindrome")
else:
    print("Palabra no es palindrome")