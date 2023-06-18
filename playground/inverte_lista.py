def inverteLista(lista):
    tamanho = len(lista)
    limite = tamanho // 2
    for j in range(limite):
        aux = lista[j]
        lista[j] = lista[tamanho-1-j]
        lista[tamanho-1-j] = aux


minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Lista não invertida")
for i in range(len(minha_lista)):
    print(minha_lista[i], end=" ")

inverteLista(minha_lista)

print("\nLista invertida")
for i in range(len(minha_lista)):
    print(minha_lista[i], end=" ")
