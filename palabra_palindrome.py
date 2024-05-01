# Tarea: generar una funcion que determine si una palbra es palindrome o no

 
def is_palindrome(palabra):
    # TODO: completar funcion
    lista = palabra
    i = 0
    j = len(lista) - 1
    pal = True
    while i < j:
        if lista[j] != lista [i]:
            pal = False
            break
        i += 1
        j -= 1
    return pal

# XXX: palabras palindromos: reconocer , anilina , arriba , ana 
# none , poto , amor

lista_test = [ ("reconocem",False) ,("anilina",True) ,
           ("none",False) , ("poto",False) , ("arriba",False) ,("ana", True) ,
           ("caca",False) , ("level" ,True) ]

for test_palabra in lista_test:
    if is_palindrome(test_palabra[0]) == test_palabra[1]:
        print(f"👌 -> Palabra {test_palabra[0]} deberia ser {test_palabra[1]}")
    else:
       print(f"❌ -> Palabra {test_palabra[0]} deberia ser {test_palabra[1]}")