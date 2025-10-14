import random

palabras = ["python", "programa", "codigo", "desafio", "computadora"]
palabra_secreta = random.choice(palabras)
palabra_actual = ["_"] * len(palabra_secreta)
intentos = 6
letras_usadas = []

print("¡Bienvenido al juego de Adivina la Palabra!")
print(f"La palabra tiene {len(palabra_secreta)} letras\n")

while True:
    print(f"Te quedan: {intentos} intentos")
    print(" ".join(palabra_actual))
    
    if letras_usadas:
        print(f"Letras usadas: {', '.join(sorted(letras_usadas))}")
    
    letra = input("Adivina una letra: ").lower()
    
    # Validar que sea una sola letra
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa solo una letra.\n")
        continue
    
    # Verificar si la letra ya fue usada
    if letra in letras_usadas:
        print("Ya usaste esa letra. Intenta con otra.\n")
        continue
    
    letras_usadas.append(letra)
    
    # Verificar si la letra está en la palabra secreta
    if letra in palabra_secreta:
        print(f"¡Bien! La letra '{letra}' está en la palabra.\n")
        # Actualizar palabra_actual con las posiciones correctas
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                palabra_actual[i] = letra
    else:
        print(f"Lo siento, la letra '{letra}' no está en la palabra.\n")
        intentos -= 1
    
    # Verificar si ganó
    if "_" not in palabra_actual:
        print("=" * 40)
        print(f"¡FELICIDADES! ¡Ganaste!")
        print(f"La palabra era: {palabra_secreta}")
        print("=" * 40)
        break
    
    # Verificar si perdió
    if intentos == 0:
        print("=" * 40)
        print("¡Perdiste!")
        print(f"La palabra era: {palabra_secreta}")
        print("=" * 40)
        break