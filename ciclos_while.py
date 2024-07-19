#Sintax:
"""""
while condicion:
    codigo
"""""
#ejercicio 1: imprime de 0-10
"""""
num = 0
while num < 10:
    print(num)
    num = num+1
"""""

#ejercicio 2: cuanta del 0 al 20 de 2 en 2
"""""
num = 0
while num <= 20:
    print(num)
    num = num+2
"""""

#ejercicio 3:
"""""
Precio de objeto al comprar?
cantidad de ese objeto?
quiere comparar otro objeto (si/no)
si teclea si el debe volver a preguntar todo denuveo
si teclea no mostrar cantidad de objetos y precio total
"""""


total_objects = 0
total_price = 0
while True:
    precio = int(input("Precio del objeto: "))
    cantidad = int(input("Cantidad: "))
    total_objects = total_objects + cantidad
    total_price = total_price + precio * cantidad
    pregunta = input("Desea comprar otro obejeto (si/no): ")
    if pregunta.lower() == "no":
        print(f"La cantidad de objetos es {total_objects} y el precio total es {total_price} dolares")
        break
    
    elif pregunta.lower()== "si":
        continue
        
    else:
        print("Opcion no valida")


