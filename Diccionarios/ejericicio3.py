#Combina diccionarios

def combina_diccionarios(dicc_1:dict[str,int], dicc_2: dict[str,int])-> dict[str,int]:
    diccionario={}
    for llave,valor in dicc_1.items():
        diccionario[llave] = valor + dicc_2.get(llave,0)
    for llave,valor in dicc_2.items():
        diccionario[llave]= valor+dicc_1.get(llave,0)
    return diccionario

dicc_1={"a":1,"b":2}
dicc_2={"b":3,"c":4}
print(combina_diccionarios(dicc_1,dicc_2))  #Salida:


