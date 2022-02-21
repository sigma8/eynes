from random import randint

def matriz(n: int):
    return [([(randint(1, n)) for x in range(5)]) for y in range(5)]

# Verifica que una lista sea consecutiva
def esconsecutivo(listas: list):
    return sorted(listas) == list(range(min(listas), max(listas)+1))

# Crea funcion que invierte matriz para evaluar si es consecutiva
def vertical(lista: list):
    return list([[new_list[i] for new_list in lista] for i in range(5)])

# Revisar si existe o no una secuencia consecutiva de numeros vertical u horizontalmete
def check(listas: list):
    result, result_2 = "No, existe", "No Existe"
    for i, lista in enumerate(listas):
        if esconsecutivo(lista) == True:
            result = f"Posicion inicial: {[i, lista.index(min(lista))]}, Posicion final: {[i, lista.index(max(lista))]}"           
    for j, lista in enumerate(vertical(listas)):
        if esconsecutivo(lista) == True:
            result_2 = f"Posicion inicial: {[lista.index(min(lista)),j]}, Posicion final: {[lista.index(max(lista)), j]}"
    return(result, result_2)
