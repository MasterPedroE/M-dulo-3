from tremnovo import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, data_nascimento, sexo, matricula):
        super().__init__(nome, data_nascimento, sexo)
        self.matricula = matricula

aluno1 = Aluno("João Silva", "10/01/2005", "Masculino", "2021001")

print("******* Dados do aluno *******")
print("Matrícula: ", aluno1.matricula)
print("Nome: ", aluno1.nome)
print("Data de nascimento: ", aluno1.data_nascimento)
print("Sexo", aluno1.sexo)