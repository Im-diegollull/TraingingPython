#open(): Siempre cerrar el archivo al cerrar

#archivo = open(nombre_del_archivo)
#archivo = open(nombre_del_archivo,  modo)

# 4 modos de archivos
# r: Cuando solo quieres leer el archivo 
#               -si no existe archivo marca error
# w: Cuando quieres escribir en el archivo, si existe lo sobreescribe.
#               -si no existe archivo lo crea
# a: Cuando quieres escribir en el archivo, si existe lo agrega al final
#               -si no exite el archivo, lo crea
# r+: Cuando queires leer y escribir, no borra ni sobre escribe si ya existe
#               -si no exite archivo amarca error

#ESCRIBIR ARICHVO:
#archivo.write("Hola mundo")

#MINI EJERCICIO
#Escribe un programa que lea un archivo y lo muestre en pantalla

archivo = open('prueba.text','w')
archivo.write("Hola esta es la linea 0\n")
archivo.write("Hola esta es la linea 1\n")
archivo.write("Hola esta es la linea 2\n")
archivo.close()

#Lextura de Archivos

# metodos de lectura de archivos
# read(): Lee todo el archivo, Si el archivo es muy grande, puede que no se pueda leer todo en memoria
# readline(): Lee una linea del archivo
# readlines(): Lee todas las lineas del archivo y las devuelve en una lista
# in: itera liena por liena el archivo
# ENTER: \, todas las lienas de un archivo tienen un enter al final

#read()
print('Leyendo el archivo usando read\n')
archivo = open('prueba.text','r')
todo_el_archv = archivo.read()
print(todo_el_archv)
archivo.close()

#readline()
print('Leyendo el archivo usando readline\n')
archivo = open('prueba.text','r')
primera_linea = archivo.readline()
segunda_linea = archivo.readline()
tercera_linea = archivo.readline()
print(primera_linea, end='')
print(segunda_linea, end = '')
print(tercera_linea, end = '')
archivo.close()

# in
print('Leyendo el archivo usando in\n')
archivo = open('prueba.text','r')
for linea in archivo:
    print(linea, end = '')
archivo.close()

# with
with open('pruebas.txt','w') as archivo:
    archivo.write('linea 0\n')
    archivo.write('linea 1\n')
    archivo.write('linea 2\n')

# lectura
with open('pruebas.txt','r') as archivo:
    print(archivo.read())


