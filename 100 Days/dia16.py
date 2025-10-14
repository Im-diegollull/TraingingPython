palabra = "Hola hola mundo mundo Python"
lista = []

palabras = palabra.split()


for palabra in palabras:
    p_lower = palabra.lower()  
    if p_lower not in lista:
        lista.append(p_lower)

print("Palabras únicas:", lista)
print("Número de palabras únicas:", len(lista))
        
    
        
