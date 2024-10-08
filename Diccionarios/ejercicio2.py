def cuenta_letras(str):
    diccionario = {}
    for letra in str:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    return diccionario
print(cuenta_letras('hola mundo'))