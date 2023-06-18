def soma_recursiva(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    return arr[0] + soma_recursiva(arr[1:])


minha_lista = [10, 20, 30, 50, 100]
print(soma_recursiva(minha_lista))
