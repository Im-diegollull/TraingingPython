#lista = [1,2,3,4,5,6,7,8,9,10]
#lista_cuadrado = []

#for valor in lista:
#    lista_cuadrado.append(valor**2)
#print(lista_cuadrado)


#lista = [1,2,3,4,5,6,7,8,9,10]
#lista_cuadrado = [valor**2 for valor in lista]
#print(lista_cuadrados)

#Ejemplo 2
lista = [1,2,3,4,5,6,7,8,9,10]
lista_pares = []
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i**2)
print(lista_pares)

lista = [1,2,3,4,5,6,7,8,9,10]
lista_pares = [i**2 for i in lista if i % 2 == 0]
print(lista_pares)