# day 3 programing python
#Detectar palindromos
def es_palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    return palabra == palabra[::-1]
#Ejemplo de uso
palabra = input("Dame una palabra: ")
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")