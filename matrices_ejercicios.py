#Ejercicio 1:
'''
Cree una funcion llamada sustituye matriz()que va a 
recivir un numero entero N y una matriz. Deberas 
sustituir todas los numeros que sean multiplo del numero N 
con -1(un numero multiplo de n el residual da 0)

def sustituye_matriz(N, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % N == 0:
                matriz[i][j] = -1
    return matriz
    
print(sustituye_matriz(5,[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))
'''
#Ejercicio 2:
'''
Crea una funcion llamada aplana
que reciba una matriz y devuelva una lista con 
todos los elementos de la matriz ordenados.

def aplana(matriz):
    nueva_matriz = []
    for  i in range(len(matriz)):
        for j in range(len(matriz)):
            nueva_matriz.append(matriz[i][j])
            
    return sorted(nueva_matriz)

print(aplana([[5,4],[3,2]]))
'''   
#Ejercicio 3:
'''
Cree una funcion llamada imprime matriz
que imprima la matriz de forma bonita ej:
1 2 3
4 5 6

def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print()

imprime_matriz([[1,2,3],[4,5,6],[7,8,9]])

def imprimeMatriz(matriz):
    for fila in matriz:
        for num in fila:
            print(num, end =' ')
        print()

imprimeMatriz([[1,2,3],[4,5,6],[7,8,9]])
'''
#Ejercicio 4:
'''
Crea una funcion  llamadas dibuja curz
dada una matriz de la misma cantidad de filas que de columnas 
compuesta por solo 1´s. Dibuja una cruz(x) que cruz por
el centro de la matriz 
'''
def dibuja_x(matriz):
    n = len(matriz)  #
    
    for i in range(n):
        for j in range(n):
          
            if i == j or i + j == n - 1:
                print('0', end='')
            else:
                print('1', end='')
        print()  

# Ejemplo de uso
dibuja_x([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])


#Ejercicio 5:


# 0,0 0,1 0,2 0,3    3,0 2,1 1,2 0,3
# 1,0 1,1 1,2 1,3
# 2,0 2,1 2,2 2,3
# 3,0 3,1 3,2 3,3