def conta_elementos_array(lista):
    if not lista:
        return 0
    if len(lista) == 1:
        return 1
    return 1 + conta_elementos_array(lista[1:])


minha_lista = [20, 30, 40, 50, 90, 100, 200, 230, 500, 1, 10, 11]
print(conta_elementos_array(minha_lista))
