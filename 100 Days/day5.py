#numero repetido en una lista

def non_repeted_number_in_list(lista):
    """
    Given a list of integers, find the first non-repeated number in the list.
    """
    for i in lista:
        if lista.count(i) == 1:
            return i
    return None

def encontrar_unico(lista):
    resultado = 0
    for num in lista:
        resultado ^= num
    return resultado
