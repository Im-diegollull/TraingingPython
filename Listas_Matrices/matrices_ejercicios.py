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
'''

#Ejercicio 5:
'''
Dado a una matriz y dos numeros i y j
crea una funcion llmada conquista() que conquiste
las celadas alrededor del elemento matriz[i][j].
Se dice que una posicion ha sido conquistada si las
celdas adyacentes(de alrededor)
reutuliza la funcion imprime matriz

def imprime_matriz(matriz):
    for fila in matriz:
        for num in fila:
            print(num, end =' ')
        print()

def conquista(i, j, matriz):
    n = len(matriz)
    # Conquista las celdas adyacentes
    for x in range(max(0, i-1), min(n, i+2)):
        for y in range(max(0, j-1), min(n, j+2)):
            if (x, y) != (i, j):  
                matriz[x][y] = 1
    imprime_matriz(matriz)
matriz = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
conquista(1,1,matriz)  #
'''

matriz = []
for i in range(N):  
    matriz.append([])  
    for j in range(N):    
        matriz[i].append(0)