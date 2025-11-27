#contar cuantas veces aparece una letra en una frase o palabra
palabra = input("Ingresa frase o palabra: ")
palabra.lower()

diccionario = {}
for letra in palabra:
    if letra  == " ":
        continue
    if letra in diccionario:
        diccionario[letra] +=1
    else: 
        diccionario[letra]=1
    

for letra in diccionario.keys():
    valor = diccionario[letra]
    print(f'{letra}: {valor}')
        
