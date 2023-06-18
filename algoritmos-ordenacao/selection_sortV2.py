def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                # arr[i], arr[j] = arr[j], arr[i] -> Forma abreviada sem uma variável auxiliar
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
    return arr


minha_lista = [9, 5, 8, 3, 4, 2, 7, 1]

lista_ordenada = selectionSort(minha_lista)

for k in range(len(lista_ordenada)):
    print(lista_ordenada[k], end=" ")

print("\n")
print(selectionSort([7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1]))
