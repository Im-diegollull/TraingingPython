def es_primo(num):
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    #Verificar para el 25 o 49s
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


num = int(input("Dame un número entero positivo: "))
if es_primo(num):
    print(f"El número {num} es primo.")
else:
    print(f"El número {num} no es primo.")
