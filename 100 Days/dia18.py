#Lista de cuadrados

n = int(input("indique hasta donde quiere que lleguen los cudarados (: "))
lista_cuadrados = []

for i in range(1,n+1):
    lista_cuadrados.append(i**2)
print(lista_cuadrados)
