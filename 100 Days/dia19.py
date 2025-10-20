#numero secreto
import random

numero_secreto = random.randint(1, 100)
print(numero_secreto) # verficar wining condition
intentos  = 7
while intentos > 0:
    num = int(input("Adivina el numeron entre 1 al 100: \n"))
    intentos = intentos -1
    print(f"Te quedan {intentos} intentos \n")
    diferencia = abs(num - numero_secreto)
    if num == numero_secreto:
        print(f"haz ganado!! en tan solo {intentos} intentos")
        break
    
    if intentos == 0:
        print(f"haz perdido el numero era {numero_secreto} :( ")
        break
    
    if diferencia < 5:
        print("estas muy cerca \n")
    
    elif diferencia < 10:
        print("Estas cerca \n")
    
    else:

        print('estas lejos \n')



