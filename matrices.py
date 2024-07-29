# Matrices: 

#1. Manera manual
'''
matriz = [[1,2,3],[4,5,6],[7,8,9]]
matrz2 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
'''
#2. Manera Automatica
'''
tamaño_filas =  3
tamaño_columnas = 3
for i in range(tamaño_filas):
    lista = [0]*tamaño_columnas
print(matriz)
'''

#3. Iteracion de matrices

#for loop
'''
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
for i in range(len(matriz)): # Filas
    for j in range(len(matriz[i])): # Columnas
        print(matriz[i][j])
'''

#while loop
'''
i = 0
while i < len(matriz):
    j = 0
    print(f'Entrando a la fila {i}')
    fila = matriz[i]
    while j < len(fila):
        print(matriz[i][j])
        j = j + 1
    i = i + 1
'''
#for loop secilla para leer valores
'''
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
for fila in matriz:
    for ele in fila:
        print(ele)
'''
# MINI EJERCICO
'''
 hacer una funcion llamada reset_valores(matriz)
y que resetee los valores de la matriz a 0
'''
'''
def reset_valores(matriz):
 
 for i in range(len(matriz)):
  for j in range(len(matriz[i])):
   matriz[i][j] = 0


matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
reset_valores(matriz)
print(matriz)
'''