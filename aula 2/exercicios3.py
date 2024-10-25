compra = float(input("Digite o valor da compra"))

if compra <= 2000:
    desconto1 = (compra*10) /100
    Valor = -desconto1 + compra
    print(f"parabéns! Você ganhou um desconto de R${desconto1:.2f} e tera que pagar somente R${Valor:.2f}")

elif compra > 2000 and compra <= 3000:
    desconto2 = (compra*5) /100
    Valor = -desconto2 + compra
    print(f"parabéns! Você ganhou um desconto de R${desconto2:.2f} e tera que pagar somente R${Valor:.2f}")

elif compra > 3000 and compra <= 5000:
    desconto3 = (compra*3) /100
    Valor = -desconto3 + compra
    print(f"parabéns! Você ganhou um desconto de R${desconto3:.2f} e tera que pagar somente R${Valor:.2f}")

elif compra > 5000:
    desconto4 = (compra*2) /100
    Valor = -desconto4 + compra
    print(f"parabéns! Você ganhou um desconto de R${desconto4:.2f} e tera que pagar somente R${Valor:.2f}")