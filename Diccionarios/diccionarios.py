#Diccionarios (:
capitales_dict = {
    'Argentina':'Buenos aires', #pares de llave:valor, keyvalue
    'Bolivia': 'Sucre',
    'Brasil': 'Brasilia',
    'Mexico': 'Ciudad de Mexico',
}

capital = capitales_dict['Mexico']
print(capital)
capital = capitales_dict['Brasil']
print(capital)

#Sintax
diccionario = {}
#  usamos : para asociar la llave con el valor
# usalmos , para separar cada par de llave:valor
# utlizamos [] para accesar al valor asociado

# Agragar llave nueva:
diccionario['llave3'] = 'valor3'
print(diccionario)
# eliminar llave:
del diccionario['llave3']
print(diccionario)
# modificar llave:
diccionario['llave1'] = 'nuevo valor'
print(diccionario)
# acceder a un valor:
print(diccionario['llave1'])
# acceder a un valor que no existe:
try:
    print(diccionario['llave4'])
    except KeyError:
        print('La llave no existe')
# CONDICIONES
#1. las llaves solo pueden se de tipos inmutables,
#       -numeros
#       -strings
#2. los valores puedes ser cualquier cosa
