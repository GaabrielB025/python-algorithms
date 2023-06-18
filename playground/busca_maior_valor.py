def maior_valor_iterativo(lista):
    maior = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior


def maior_valor_recursivo(lista):
    if not lista:
        return 0
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    maior = maior_valor_recursivo(lista[1:])
    return lista[0] if lista[0] > maior else maior


minha_lista = [10, 5, 3, 2, 100, 20, 50, 101, 70]
print(maior_valor_iterativo(minha_lista))
print(maior_valor_recursivo(minha_lista))
