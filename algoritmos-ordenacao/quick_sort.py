def quicksort(array):
    if len(array) < 2:
        return array
    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)


minha_lista = [5, 2, 30, 6, 10, 20, 1]
print(quicksort(minha_lista))
