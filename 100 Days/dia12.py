edad = int(input("Dime cual es tu edad: "))

if edad >= 0 and edad<= 2:
    print("ERES BEBE")
elif edad >=3 and edad<=12:
    print("ERES UN NIÑO")
elif edad >=13 and edad<=17:
    print("ERES UN adolecente")
elif edad >=18 and edad<=64:
    print("ERES UN ADULTO")
elif edad >=65:
    print("VIEJO")
else:
    print("Ingresa otro valor")