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


def pesquisaBinaria2(lista, item, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return meio
        if item < lista[meio]:
            return pesquisaBinaria2(lista, item, inicio, meio-1)
        else:
            return pesquisaBinaria2(lista, item, meio+1, fim)
    return None


minha_lista = [1, 2, 5, 7, 9]
print(pesquisaBinaria(minha_lista, 7))  # => 7
print(pesquisaBinaria2(minha_lista, 7))  # => 3
