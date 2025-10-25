#contar pares e impartes

lista  = [1,2,3,4,5,6,7,8,9,10]
contar_pares = 0
contar_impares = 0

for pares in lista:
    if pares % 2 == 0:
        contar_pares += 1
    else:
        contar_impares += 1
print(f"la cantidad de numero pares en la lista son: {contar_pares}")
print(f"la cantidad de numero impares en la lista son: {contar_impares}")

#mostrar palabra al revez

palabra = input("Digame la palabra que quiera: ")
print(palabra[::-1])



#ejercicio 3 promedio de una lista

def promedio(lista):
    
    suma = 0
    suma = sum(lista)
    elementos = len(lista)
    
    avg = suma/elementos
    print(f"El promedio de los elementos de esta lista es: {avg}")
lista  = [1,2,3,4,5,6,7,8,9,10]
promedio(lista)


    