class Produto:
    def __init__(self, codproduto, nome, descricao, tamanho, preco):
        self.codproduto = codproduto
        self.nome =  nome
        self.descricao = descricao
        self.tamanho = tamanho
        self.preco = preco

    def desconto (self, custo):
        custo = -(self.preco * 0.10) + self.preco
        print(f"Contando com o desconro, o produto: {self.nome} fica custando apenas: R$ {custo:.2f}")

produtos = []

while True:
    tipo = input("Para cadastrar presione qualquer tecla ou Digite S para sair: ")

    if tipo.upper() == "S":
        break

    codproduto = input("Digite o código do produto: ")
    nome =  input("Digite o nome: ")
    descricao = input("Digite a descrição: ")
    tamanho = input ("Digite o tamanho: ")
    preco = input ("Digite o preço: ")

    produto = Produto(codproduto, nome, descricao, tamanho, preco)

    produtos.append(produto)


print("Lista de Produtos: ")
for prod in produtos:
    print(prod.nome, "-", prod.descricao, "-", prod.tamanho, "-", prod.preco)