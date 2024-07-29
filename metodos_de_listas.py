#Metodos de listas

#APPEND
lista = [1,2,3,4]
lista.append(40)
print(lista)

lista2 = [5,6,7,8]
lista.extend(lista2)
print(lista)
#INSERT
lista3 = [1,2,4]
lista3.insert(2,3)
print(lista3)

#REMOVE
lista4 = [1,2,3,4,5]
lista4.remove(3)
print(lista4)

#SORT:menor a mayor
lista5 = [5,2,8,1,9]
lista5.sort()
print(lista5)

#COPY
lista6 = [1,2,3,4,5]
lista7 = lista6.copy()
print(lista7)

#Index
lista8 = [1,2,3,4,5]
print(lista8.index(3))

