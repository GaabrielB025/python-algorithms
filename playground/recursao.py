def regressao(i):
    print(i)
    if i <= 1:
        return
    return regressao(i - 1)


regressao(10)
