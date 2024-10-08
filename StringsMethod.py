#strings method

#palabra.lower(): palabra a minusculas



#palabra.strip(): te regresa una palabra pero te quita 
# los caracteres en blanco tambien se pueden quitar signos:
# strip("!")
"""
palabra = "     hola "
limpia = palabra.strip()
print(palabra)
print(limpia)
"""


#palabra.startwith("prefijo") empieza con la palabra que tu quieras
#palabra.endwith("sufijo") termina
"""
pagina_web = "www.daga.com"
es_pagina = pagina_web.startswith("www")
es_pag = pagina_web.endwith("com")
print(es_pagina)
"""
#palabra.upper(). todo en mayuscula


#palabra.replace(
"""
oracion = "La persona llega"
corregido = oracion.replace("llega", "se va")
print(corregido)
"""

#palabra.isalpha() tiene solo letras true or false
"""
palabra = "perroabc"
palabra_num = "perro123"
es_palabra = palabra.isalpha()
no_es_palabra = palabra_num.isalpha()
print(es_palabra)
print(no_es_palabra)
"""
#palabra.isdigit() si la palabra es digito

#1.palabra.find() palabra que quieres buscar uwu
#2.palabra.count() cuantas veces aparece la palabra

#1
"""
oracion = "hola como estas me llamo aaron"
posicion=oracion.find("aaron")
print(posicion)
posicion = oracion.find("hector")
print(posicion)
"""
#2
"""
oracion = "hola como estas me llamo aaron"
existe = "aaron" in oracion
print(existe)
"""
#1 efe stings xd
"""
palabra1 = "hola"
palabra2 = "Mundo"

oracion = f"{palabra1} {palabra2}"
print(oracion)
print = hola mundo

"""
#2
"""
nombre = "diego"
edad = 22
oracion = f"mi nombre es {nombre} y tengo {edad} años"
print(f"mi nombre es {nombre} y tengo {edad} años")
print(oracion)
"""
"""
palabra= "HOLA"
palabra = palabra.lower()

print(palabra)
"""

#ultimas dos letras de una palabra
#ejemplo (samurai, ai)
def solution(text, ending):
    return text.endswith(ending)
print(solution("samurai",'ai'))



    
   
