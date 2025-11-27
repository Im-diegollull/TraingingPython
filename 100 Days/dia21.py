# es palindromo

def es_palindromo():
    palabra = input("Ingrese una frase o palabra: ")
    if palabra.lower() == palabra.lower()[::-1]:
        print("Es palindromo")
    else:
        print("No es palindromo")
    

es_palindromo()