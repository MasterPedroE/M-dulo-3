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
        

    

produto1 = Produto("P1845", "Micro-ondas", "Place Holder", "500x300", 1000)
produto2 = Produto("H3795", "Computador", "Place Holder", "200x2000", 2000)
produto3 = Produto("Y46752", "Vídeo game", "Place Holder", "100X200", 5000)



print(f"Código: {produto1.codproduto} Nome do Produto: {produto1.nome} Descrição do produto: {produto1.descricao} Tamanho do produto: {produto1.tamanho} Preço: R${produto1.preco:.2f}")
print("-------------------------------------------------------------------------------------------------------------------------")
print(f"Código: {produto2.codproduto} Nome do Produto: {produto2.nome} Descrição do produto: {produto2.descricao} Tamanho do produto: {produto2.tamanho} Preço: R${produto2.preco:.2f}")
print("-------------------------------------------------------------------------------------------------------------------------")
print(f"Código: {produto3.codproduto} Nome do Produto: {produto3.nome} Descrição do produto: {produto3.descricao} Tamanho do produto: {produto3.tamanho} Preço: R${produto3.preco:.2f}")
print("-------------------------------------------------------------------------------------------------------------------------")

produto1.desconto("aaa")
produto2.desconto("aaa")
produto3.desconto("aaa")