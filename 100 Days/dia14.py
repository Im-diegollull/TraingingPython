#Contar palabras y poner todo alrevez

frase = "Hola mundo programando en Python"

contador = len(frase.split())
print(f"La canitdad de palabras en-> {frase}: son {contador}")


palabras = frase.split()
frase_alrevez = " ".join(palabras[::-1])
print(frase_alrevez )




