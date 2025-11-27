#Encotnrar al numero mas grande en una lista

lista = [4, 10, 2, 8, 10, 3]

mayor = lista[0]
actual = None

for actual in lista:
    if actual > mayor:
        mayor = actual
    else:
        continue
print(f"el numero mas grande de la lista es: {mayor}")
    
