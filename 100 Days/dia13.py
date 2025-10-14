#Devuelve solo primos

lista = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
lista_primos = []


for num in lista:
    if num < 2:
        continue
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):  # revisa divisores hasta √num
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        lista_primos.append(num)

print(lista_primos)


