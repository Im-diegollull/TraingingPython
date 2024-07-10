def marcador(jugador1, jugador2, sets_jugador1, sets_jugador2, juegos_jugador1, juegos_jugador2, puntos_jugador1, puntos_jugador2, advantage):
    # Función para mostrar el marcador actual
    print(f"Marcador: {jugador1} vs {jugador2}")
    print(f"Sets: {sets_jugador1} - {sets_jugador2}")
    print(f"Juegos: {juegos_jugador1} - {juegos_jugador2}")

    # Representación visible de los puntos en tenis
    puntos_visibles = ["0", "15", "30", "40"]

    # Manejo de la puntuación cuando ambos jugadores están en 40 puntos (deuce) o ventaja
    if puntos_jugador1 >= 3 and puntos_jugador2 >= 3:
        if advantage == jugador1:
            print(f"Puntos: AD - 40")  # Jugador 1 tiene ventaja
        elif advantage == jugador2:
            print(f"Puntos: 40 - AD")  # Jugador 2 tiene ventaja
        else:
            print(f"Puntos: 40 - 40")  # Ambos están en deuce (40-40)
    else:
        # Mostrar puntos estándar (0, 15, 30, 40)
        print(f"Puntos: {puntos_visibles[puntos_jugador1]} - {puntos_visibles[puntos_jugador2]}")

def main():
    # Solicitar nombres de los jugadores
    jugador1 = input("Ingrese el nombre del jugador 1: ")
    jugador2 = input("Ingrese el nombre del jugador 2: ")

    # Inicializar los contadores de sets, juegos y puntos
    sets_jugador1 = 0
    sets_jugador2 = 0
    juegos_jugador1 = 0
    juegos_jugador2 = 0
    puntos_jugador1 = 0
    puntos_jugador2 = 0
    advantage = None  # Variable para almacenar quién tiene la ventaja

    # Bucle principal del juego que continúa hasta que uno de los jugadores gane 2 sets
    while sets_jugador1 < 2 and sets_jugador2 < 2:
        # Mostrar el menú de opciones
        print(f"\n1. Anotar punto a {jugador1}")
        print(f"2. Anotar punto a {jugador2}")
        print("3. Mostrar marcador")
        print("4. Salir")

        # Leer la opción del usuario
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            # Anotar punto a jugador 1
            if puntos_jugador1 >= 3:  # Si el jugador 1 ya tiene 3 puntos (equivalente a 40)
                if puntos_jugador2 >= 3:  # Si ambos tienen al menos 3 puntos (deuce o ventaja)
                    if advantage == jugador1:  # Jugador 1 ya tiene ventaja
                        juegos_jugador1 += 1  # Gana el juego
                        puntos_jugador1 = 0
                        puntos_jugador2 = 0
                        advantage = None  # Resetear ventaja
                    elif advantage == jugador2:  # Jugador 2 tenía ventaja
                        advantage = None  # Vuelve a deuce
                    else:
                        advantage = jugador1  # Jugador 1 obtiene la ventaja
                else:
                    juegos_jugador1 += 1  # Jugador 1 gana el juego
                    puntos_jugador1 = 0
                    puntos_jugador2 = 0
            else:
                puntos_jugador1 += 1  # Incrementar puntos de jugador 1
        elif opcion == "2":
            # Anotar punto a jugador 2
            if puntos_jugador2 >= 3:  # Si el jugador 2 ya tiene 3 puntos (equivalente a 40)
                if puntos_jugador1 >= 3:  # Si ambos tienen al menos 3 puntos (deuce o ventaja)
                    if advantage == jugador2:  # Jugador 2 ya tiene ventaja
                        juegos_jugador2 += 1  # Gana el juego
                        puntos_jugador1 = 0
                        puntos_jugador2 = 0
                        advantage = None  # Resetear ventaja
                    elif advantage == jugador1:  # Jugador 1 tenía ventaja
                        advantage = None  # Vuelve a deuce
                    else:
                        advantage = jugador2  # Jugador 2 obtiene la ventaja
                else:
                    juegos_jugador2 += 1  # Jugador 2 gana el juego
                    puntos_jugador1 = 0
                    puntos_jugador2 = 0
            else:
                puntos_jugador2 += 1  # Incrementar puntos de jugador 2
        elif opcion == "3":
            # Mostrar el marcador actual
            marcador(jugador1, jugador2, sets_jugador1, sets_jugador2, juegos_jugador1, juegos_jugador2, puntos_jugador1, puntos_jugador2, advantage)
        elif opcion == "4":
            break  # Salir del programa
        else:
            print("Opción inválida. Intente nuevamente.")

        # Verificar si alguno de los jugadores ha ganado un set
        if juegos_jugador1 >= 6 and juegos_jugador1 - juegos_jugador2 >= 2:
            sets_jugador1 += 1
            juegos_jugador1 = 0
            juegos_jugador2 = 0
        elif juegos_jugador2 >= 6 and juegos_jugador2 - juegos_jugador1 >= 2:
            sets_jugador2 += 1
            juegos_jugador1 = 0
            juegos_jugador2 = 0

        # Mostrar el marcador después de cada punto
        marcador(jugador1, jugador2, sets_jugador1, sets_jugador2, juegos_jugador1, juegos_jugador2, puntos_jugador1, puntos_jugador2, advantage)

    # Anunciar el ganador del partido
    if sets_jugador1 == 2:
        print(f"¡{jugador1} es el ganador del partido!")
    elif sets_jugador2 == 2:
        print(f"¡{jugador2} es el ganador del partido!")
    else:
        print("El partido se suspendió")

if __name__ == "__main__":
    main()
