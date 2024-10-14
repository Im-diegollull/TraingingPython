# if-else -->a or -->b

# Operador ternario
#programa que pone hola si el usuario es mayor o oigual a 21 años sino bye
def dame_palabra(edad:int):
    texto_a_impirmir = ""

    if edad >= 21:
        texto_a_imprimir = "hola"
    else:
       texto_a_imprimir = "adios"
    return texto_a_imprimir


def dame_palabra_v2(edad:int):
    texto_a_imprimir = "hola" if edad >= 21 else "adios"
    return texto_a_imprimir
def dame_palabra_v3(edad:int):
    return "hola" if edad >= 21 else "adios"

print(dame_palabra(21))
print(dame_palabra_v2(21))
