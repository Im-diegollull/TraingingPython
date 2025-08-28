
def sumar_pares(n):
    suma = 0
    for i in range(n + 1):
        if i % 2 == 0:
            suma += i
    return suma
n = int(input("Ingrese un número: "))
print(sumar_pares(n))