def pesquisaBinaria(lista, item):
    alto = len(lista) - 1
    baixo = 0

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return chute
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


minha_lista = [1, 2, 5, 7, 9]
print(pesquisaBinaria(minha_lista, 7))
