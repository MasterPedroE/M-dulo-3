class Pessoa:
    def __init__(self, nome, data_nascimento, sexo):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo

    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}")

pessoa1 = Pessoa("José", "20/10/1995","masculino")
pessoa2 = Pessoa("Maria", "15/01/2001","feminino")

print("Nome", pessoa1.nome,"Data de Nascimento",pessoa1.data_nascimento)
print("Nome", pessoa2.nome,"Data de Nascimento",pessoa2.data_nascimento)