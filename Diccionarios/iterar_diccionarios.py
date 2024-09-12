diccionario = {
    'Aaron': 23,
    'Alejandro': 24,
    'Antonio': 27,
    'Agustin':22,
}

# Iterando por las llaves
# keys()
for nombre in diccionario.keys():
    valor = diccionario[nombre]
    print(f'{nombre}->{valor}')

# Interando por los valores
# values()
for valor in diccionario.values():
    print(valor)

# Iterar por llave y valor
# items()
for llave, valor in diccionario.items():
    print(f'{llave}->{valor}')
    
    
