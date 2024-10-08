#Ejercicio1
#Escribe un funcio que reciba un diccionario tipo str,int
#y que regrese 

def llave_existe(dicc:dict[str, int]):
    llave = input('Escribe la llave que quieras buscar: ')
    if llave in dicc:
        return True
    else:
        return False
mi_diccionario = {"uno": 1, "dos": 2, "tres": 3}
print(llave_existe(mi_diccionario))

#Ejercicio2