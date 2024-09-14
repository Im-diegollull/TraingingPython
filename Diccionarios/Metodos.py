#Metodos de diccionarios
# get(llave): accesar al diccionario de manera segura
#diccionario = {'llave1': 'valor1'}
#valor = diccionario['llave2']
#valor = diccionario.get('llave2')
#print(valor)

#valor = diccionario.get('llave3', -1)
#if valor == -1:
    #print('La llave no existe')
    #print(valor)

#Copy(): regresa una copia del diccionario
#diccionario2 = diccionario.copy()
#print(diccionario2)

#items(): iterar por valor y llave a mismo tiempo
#for llave, valor in diccionario.items():
    #print(f'La llave es {llave} y el valor es {valor}')

# keys(): iterar por llave
#for llave in diccionario.keys():
    #print(llave)

# values(): iterar por valor
#for valor in diccionario.values():
    #print(valor)


#pop(llave): elimina el par llave: el valor que esta asociado con esa llame y regresa el valor

#diccionario = {
    #'llave1': 'valor1',
    #'llave2': 'valor2',
    #'llave3': 'valor3'
#}
#valor_borrado = diccionario.pop('llave2')
#print(f'El valor borrado es {valor_borrado}')
#print(diccionario)


#Popitem(): elimina el ulitmo para llave:valor que se agrego al dicc y regresa el par llave:valor

diccionario = {
    'llave1': 'valor1',
    'llave2': 'valor2',
    'llave3': 'valor3'
}
diccionario['llave4'] = 'valor4'
llave_valor_borrado = diccionario.popitem()
print(f'El valor borrado es {llave_valor_borrado}')
print(diccionario) 