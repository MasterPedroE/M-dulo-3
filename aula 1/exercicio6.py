#43% custa fabricção
#restante guarda 15% conta
#15% coverte para euro

pao = 0.80
qntpao = 0
broa = 2.50
qntbroa = 0
resposta = "Sim"


while resposta == "Sim" or resposta == "sim":
    pedido = input("O que o cliente deseja?")
    if pedido == "Pão" or pedido == "pão":
        qntpao += 1
    elif pedido == "Broa" or pedido == "broa":
        qntbroa += 1
    
    resposta = input("Ainda tem mais um cliente, Sr João?")

lucro = (pao * qntpao) + (broa * qntbroa)
fabricacao = (lucro *43) / 100
poupanca = (lucro *15) / 100
converter = (lucro *15) / 100
euro = converter / 6.16


print(qntpao,"pães foram vendidios")
print(qntbroa,"broas foram vendidas")

print ("R$",lucro,"foi o lucro")
print ("R$",fabricacao, "foi o custo de fabricação")

print("R$",poupanca, "irá ir para poupança")
print("R$",converter, "serão convertidos em euro, que vai ficar €", euro)