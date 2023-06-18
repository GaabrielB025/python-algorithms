import random


def bubbleSort(lista):
    size = len(lista) - 1
    for j in range(size):
        for i in range(size):
            if lista[i+1] < lista[i]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
        size -= 1


lista_pequena = [2, 5, 1, 4, 0]
lista_desordenada = [11, 5, 8, 50, 30, 1, 2, 10, 0, 3, 4]
lista_repetida = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1]
lista_aleatoria = random.sample(range(1, 1000), 30)

bubbleSort(lista_pequena)
bubbleSort(lista_desordenada)
bubbleSort(lista_repetida)
bubbleSort(lista_aleatoria)

print(lista_pequena)
print("\n")
print(lista_desordenada)
print("\n")
print(lista_repetida)
print("\n")
print(lista_aleatoria)
