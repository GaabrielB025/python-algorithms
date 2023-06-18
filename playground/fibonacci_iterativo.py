primeiroTermo = 0
segundoTermo = 1

print(primeiroTermo, end=" ")
print(segundoTermo, end=" ")

auxiliar = 3
termo = 15

while auxiliar <= termo:
    termoAtual = primeiroTermo + segundoTermo
    primeiroTermo = segundoTermo
    segundoTermo = termoAtual
    auxiliar += 1
    print(termoAtual, end=" ")
