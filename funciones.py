#sintax
'''
def numobre_de_la_funcion(parametros):

    codigo
'''
#Ejemplo: crea funcion suma y que te regrese el resultado
'''
def suma(a,b):
    return a+b

resultado = suma(2,3)
print(f'El resulatdo de la suma es: {resultado}')
'''

#Ejemplo_2: 
# crea funcion que imprima el texot que le enviemos
# pero que al principio escriba nuestro nombre
'''
def imprimir(texto, nombre):

    print(f'{nombre} {texto}')

imprimir('Hola mundo', 'Juan')
'''
#Tipado de funciones:
'''
def suma(a: int, b: int) -> int:
    return a+b
resultado = suma(2,3)
print(f'El resulatdo de la suma es: {resultado}')

def imprime(texto: str) -> None:
    print(texto)
    imprime(f"Diego, {texto}")
'''
#Tipos de datos:
'''
x: int = 1
y: float = 2.5
z: str = 'Hola mundo'
b: bool = True
'''

#SCOPES
'''
def imprimir_num():
    global x
    x = 10
    print(f'El valor de x es: {x}')
x=20
imprimir_num()
print(x)
'''
#Ejercicio 1:
'''
Realiza una funcion que recive un str y cuenta vocales
'''
'''
def cont_voc(palabra):
    vocales = 'aeiou'
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador = contador +1
    return contador
   
        
print(cont_voc('hola'))
'''
#Ejercicio 2:
'''
Realiza una funcion que recive una palabra y que le quita las vocales
'''
'''

def quita_vocales(palabra):
    vocales = 'aeiou'
    nueva_palabra = ''
    for letra in palabra:
        if letra not in vocales:
            nueva_palabra = nueva_palabra + letra
    return nueva_palabra

print(quita_vocales('hola'))
print(quita_vocales('aeiou'))

'''
#Ejercicio 3:
'''

def es_digito(algo):
    num = '1234567890'
    for letra in algo:
        if letra in num:
            return True
        else:
            return False
print(es_digito('1'))
print(es_digito('a'))
print(es_digito('a1'))
'''

#Ejercico 4:

'''
def quita_digitos(palabramixta):
    nueva_palabra = ''
    num = '1234567890'
    for letra in palabramixta:
        if letra not in num:
            nueva_palabra = nueva_palabra + letra
    return nueva_palabra

print(quita_digitos('hola123'))
print(quita_digitos('h0l4'))

'''



