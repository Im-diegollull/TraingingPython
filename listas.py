                            #Listas
# Sintax
'''
lista = [1,2,3,4,5,6,7,8,9]
lista_vacia = []
'''
# Acceso y slicing
'''
print(lista[0])
print(lista[0:5])
print(lista[:])
'''
# Mutar listas
'''

lista = [10,20,30,40]
print(lista)
lista[0] = 100
print(lista)
lista[1:3] = [200,300]
print(lista)
tamaño = len(lista)
print(tamaño)
'''

# Iterando Listas


#Con while y len()

'''
lista = [1,2,3,4,5,6,7]
i = 0
while i < len(lista):
    lista[i] = 0
    i = i+1
print(lista)
'''

#Ciclo for y range

'''
lista = [1,2,3,4,5,6,7]
for i in range(len(lista)):
    lista[i] = 0
print(lista)
'''

#Ciclo for para leer
'''
list = [1,2,3,5,6,7,8]
for element in list:
    print(element)
'''

# PASO POR REFERENCIA EN LISTAS

def modificar_lista(lista: list)-> None:
    copia = lista.copy()
    copia[0] = 100
    print(f'Adentro: {copia}')

lista_og = [0,1,2,3,4,5]
modificar_lista(lista_og)
print(f'Fuera: {lista_og}')
