import random 

intentos = random.randint(7,20)

numero_elegido = random.randint(1,100)
print(f"+++Jueguemos a adivniar el num tienes {intentos-1} intentos\n")
while True:
    intentos = intentos-1
    if intentos == 0:
        print("Perdiste ya no te quedan intentos")
        break
    print(f"Te quedan {intentos} intentos\n")
    numero = int(input("Elije un numero del 1 al 100:\n "))
    
    if numero > numero_elegido:
        print("Prueba un numero mas bajo\n")
    elif numero < numero_elegido:
        print("Prueba con un numero mas grande\n")
    elif numero == numero_elegido:
        print(f"Ganaste era el numero {numero_elegido}!\n ")
        #print(f"TE DEMORASTE {intentos} intentos en conseguirlo! ")
        break
    else: 
        print("intenta otra vez")
        continue