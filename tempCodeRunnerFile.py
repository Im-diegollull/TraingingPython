# dame una funcion que diga "hola" si el usuario pone 1 y que diga "chupa el pico" si pone 0

def hola_o_chupa_el_pico() -> None:
    while True:
        opcion = int(input("Ingresa 1 si quieres que te diga hola, ingresa 0 si quieres que que te diga chupa el picoO"))
        if opcion == 1:
            print("Hola")
            
        elif opcion == 0:
            print("Chupa el pico")
        else:
            print("Opcion invalida, intenta de nuevo")

            