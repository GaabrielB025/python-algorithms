def selectionSortRecursive(lista):
    if len(lista) == 1:
        return lista

    for i in range(1, len(lista)):
        menor = lista[0]
        if lista[i] < menor:
            menor, lista[i] = lista[i], menor
            lista[0] = menor

    return [lista[0]] + selectionSortRecursive(lista[1:])


print(selectionSortRecursive([9, 5, 8, 3, 4, 2, 7, 1]))

print("\n")

lista_repetida = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1]
print(selectionSortRecursive(lista_repetida))
