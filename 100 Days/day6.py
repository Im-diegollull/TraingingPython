#Contador de vocales. 
vocales = ["a","e","i","o","u"]

def contar_vocales():
    contador = 0
    for vocal in frase:
        if vocal.lower() in vocales:
            contador += 1
    return print(contador)
frase = input("Ingrese una frase: ")
contar_vocales()