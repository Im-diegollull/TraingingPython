lista = [3, -1, 0, 7, -5, 8]
lista_postitivos = []
lista_positivos_pares = []


for numero in lista:
    if numero > 0:
        lista_postitivos.append(numero)
        if numero % 2 == 0:
            lista_positivos_pares.append(numero)




print(lista_postitivos)
print(lista_positivos_pares)