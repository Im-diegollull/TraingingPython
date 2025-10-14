
def mayor_lista(lista):
    lista.sort()
    print(f"El numero mayor de la lista es {lista[-1]}")
lista = [4, 17, 2, 33, 8, 5]

mayor_lista(lista)

def mayor(lista2):
    mayor = 0
    for num in lista:
        if num > mayor:

            mayor = num
    print(f"El número mayor es: {mayor}")
lista = [4, 17, 2, 33, 8, 5]
mayor(lista)


    
