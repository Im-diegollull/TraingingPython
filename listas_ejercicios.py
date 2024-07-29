#EJEERCICIO:1
'''
Realiza una funcion suma pares impares
dada la suma de numeros te regresa una  llista
de tamaño 2, donde la primera posicion regresa
la  suma de los pares y la sgda suma de impares
ej:[1,2,3,4,5]-->[6,9]

def suma_pares_impares(lista):
    suma_pares = 0
    suma_impares = 0
    for num in lista:
        if num % 2 == 0:
            suma_pares += num
        else:
            suma_impares += num
    print(f'[{suma_pares},{suma_impares}]')
   
suma_pares_impares([1,2,3,4,5])
'''

#EJEERCICIO:2
'''
Cree una funcion mayor que dada una lista
regrese el numero mayor de la lista

def mayor(lista):
    #metodo gei
    lista.sort()
    print(f'El numero mayor de la lista es: {lista[-1]}')

mayor([1,2,3,4,5,6])
mayor([8,5,7,20,9])


def mayor(lista):
    mayor = -100000
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

print(mayor([1,2,3,4,5,6]))
'''  
#EJEERCICIO:3
'''
cree una funcion llamada sustituye que
reciva una lista de numero enteros y un nuemro entero N
y que regrese una lista donde sustituya todos esos N por -1
ej:
sustituye(2,[2,1,3,2]) = [-1,1,3,-1]
'''
def sustituye(N,lista):
    copia = lista.copy()
    for num in range(len(copia)):
        if copia[num] == N:
            copia[num] = -1
    return copia
print(sustituye(2,[2,1,3,2]))
    