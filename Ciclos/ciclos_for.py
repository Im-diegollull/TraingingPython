#Sintax For
"""""
for variable in secuencia:
    codigo

"""""
#Ejemplo
'''
palabra = "azul"
for letra in palabra:
    print(letra)
'''

# range()
'''
Cuenta del numero de 0-10


for numero in range(11):
    #print(numero)

for numero in range(1,11):
    #print(numero)

Salto es la ultima variable

for numero in range(0,12,5):
    print(numero)

palabra = 'azul'
for contador in range(len(palabra)):
    print(palabra[contador])
'''
#Ejercicio1
'''
Crea un prrograma que pida 2 numeros enteros(a,b)
despues imprima los numero que van de a-b(incluyendo b)
se  va a ir saltando de 2 en 2

a = int(input('Dame un numero entero: '))
b = int(input('Dame otro numero entero: '))
for numero in range(a,b+1,2):
    print(numero)
'''
#Ejercicio2
'''
Crea un prrograma que pida 2 numeros enteros(a,b)
despues imprima los numero pares que van de a-b(incluyendo b)
se  va a ir saltando de 2 en 2

a = int(input('Dame un numero entero: '))
b = int(input('Dame otro numero entero: '))
for numero in range(a,b+1,2):
    if numero % 2 == 0:
        print(numero)
'''

#ejercicio3
'''
iMPRIMIR TODAS LAS VOCALES EN PALABRAS'

palabra = input("dame una palabra: ")
for letra in palabra:
    if letra in 'aeiou':
        print(letra)
     
'''
#ejercicio4
'''
Imrimir las tablas de mult hasta su mismo numero

num = int(input('dame un numero: '))
print(f"La tabla del {num}")
for mult in range(0,num+1):
    print(f"{num} x {mult} = {num*mult}")
'''
#ejercicio5
'''
imprimir las tambals de mult hasta que 


num = int(input('dame un numero: '))
print(f"La tabla del {num}")
for mult in range(0,num+1):
    for j in range(0,12+1):
        print(f"{mult} x {j} = {num*j}")
    print("+++++++++++++++")
'''

#Break y continue

#ejercicio1
'''
for i in range(1,11):
    if i == 5:
        break
    print(i)
'''
#ejercicio2
'''
for i in range(1,11):
    if i == 5:
        continue
    print(i)
'''
i = 1
while i < 100:
    print(i)
    i = i*2