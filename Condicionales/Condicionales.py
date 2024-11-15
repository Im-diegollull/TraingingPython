# Condicionales ifs
"""""
if 2<5:
    print("2 es menor que 5")
print("aqui ya estas afuera del if")
"""""

# Ejercicio 1
"""""
Preguntarle la edad al usuario e imprimirla
si la edad es >o igul a 18 iimporimir eres mayor de eadad

edad = int(input("Cual es tu edad: "))
print(f" Tu tienes {edad} años")
if edad >= 18:
    print("Eres mayor de edad")
"""""

# Condicionales if else
"""""
Preguntarle la edad al usuario e imprimirla
si la edad es >= a 18 imprimir eres mayor de eadad
si la edad es < 18 imprimir es menor de edad


edad= int(input("Ingresa tu edad: "))
print("")
print(f"Tu tienes {edad} años\n")
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
"""""
# Condiciones elif
"""""
Preguntarle la edad al usuario e imprimirla
si la edad es >= a 18 pero <64 imprimir eres mayor de eadad
si la edad es < 18 imprimir es menor de edad
si la edad es >= a 64 eres de tercera edad

edad = int(input("Ingresa tu edad: "))
print("")
print(f"Tu tienes {edad} años de edad. \n")
if edad >=65:
    print("Eres de tercera edad.")
elif edad < 18:
    print("Eres menor de edad.")

else:
    print("Eres mayor de edad")
"""""

#EJERCICIO 1
"""""
CREA UN PROGRAMA QUE LEA 3 NUM DEL USR
Y IMPRIMA CUAL ES EL MAS GRANDE DE LOS 3

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))



if num1 > num2 and num1 > num3:
    print(f"El NUMERO MAS GRANDE ES: {num1} ")
elif num2>num1 and num2>num3:
    print(f"El NUMERO MAS GRANDE ES:{num2} ")
else:
    print(f"El NUMERO MAS GRANDE ES : {num3} ")
"""""

#Ejercicio2:
"""""
EL PROFESOR QUIRE CONVERTIR LOS FUNTAJES A LETRAS
SI ES DE 90 A 100 PTS ES UNA A
SI ES DE 80 A 89 PTS ES UNA B
SI ES DE 70 A 79 PTS ES UNA C
SI ES DE 60 A 69 PTS ES UNA D
Y MENOR A 60 ES UNA F

nota= int(input("INGRESE LA NOTA DEL ALUMNO: "))
print("")

if nota >= 90 and nota <= 100:
    print(f"Tu nota con {nota} puntos es una A")
elif nota >=80 and nota <= 89:
    print(f"Tu nota con {nota} puntos es unaB")
elif nota >= 70 and nota <=79:
    print(f"Tu nota con {nota} puntos es unaC")
elif nota >=60 and nota <=69:
    print(f"Tu nota con {nota} puntos es una D")  
else:
    print(f" Tu nota con {nota} puntos es una F")
"""""
#EJERCICIO 3
"""""
Determina si un triangulo es isoceles, equilatero o escaleno

lado1 = int(input("Ingrese el primer lado de un triangulo: "))
lado2 = int(input("Ingrese el segundo lado de un triangulo: "))
lado3 = int(input("Ingrese el tercer lado de un triangulo: "))

if lado1==lado2 and lado1==lado3:
    print("Es un triangulo equilatero")
elif lado1==lado2 and lado1!=lado3 or lado1!=lado2 and lado2==lado3:
    print("Es un triangulo isosceles")
else:
    print("Es un triangulo escaleno")
"""""
num = 4 + 5*4%3

