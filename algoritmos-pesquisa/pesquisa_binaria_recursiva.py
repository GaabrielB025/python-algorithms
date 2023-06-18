def pesquisaBinariaRecursiva(lista, item, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return item
        if item < lista[meio]:
            return pesquisaBinariaRecursiva(lista, item, inicio, meio - 1)
        else:
            return pesquisaBinariaRecursiva(lista, item, meio + 1, fim)
    return None


minha_lista = [2, 5, 7, 8, 10, 12, 14, 20, 30, 55, 100]
print(pesquisaBinariaRecursiva(minha_lista, 8))
