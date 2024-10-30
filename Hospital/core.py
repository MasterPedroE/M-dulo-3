medicos = []
enfermeiros = []
funcionarios = []
resposta = ""

class Funcionario:
    def __init__ (self, matricula, nome, telefone, email, cpf, rg):
        self.matricula = matricula
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.rg = rg


class Medicos(Funcionario):
    def __init__(self, matricula, nome, telefone, email, cpf, rg, crm, atendimento, localizacao, especialidade, hora):
        super().__init__(matricula, nome, telefone, email, cpf, rg)
        self.crm = crm
        self.atendimento = atendimento
        self.localizacao = localizacao
        self.especialidade = especialidade
        self.hora =hora



class Enfermeiros(Funcionario):
    def __init__(self, matricula, nome, telefone, email, cpf, rg, coren):
        super().__init__(matricula, nome, telefone, email, cpf, rg)
        self.coren = coren
        
        
        
        
profissao = input("O fúncionarios é Médico (M) , enfermeiro (E)?\nPara outras profissões, digite qualquer outra tecla: ")

while resposta == "S" or resposta == "s":

    if profissao.lower() == "m":
        matricula = input("Digite a matricula do funcionário: ")
        nome = input("Digite o nome do funcionários: ")
        telefone = input("Digite o número de telefone do funcionario: ")
        email = input("Digite o email do funcionário: ")
        cpf = input("Digite o cpf do fucionário: ")
        rg = input ("Digite o rg do funcionário: ")
        crm = input("Digite o crm do médico: ")
        atendimento = ("Método de atendimento: ")
        localizacao = ("Localização: ")
        especialidade = ("Especialidade: ")
        hora = ("Horário de antendimento: ")

        medicos = Medicos(matricula, nome, telefone, email, cpf, rg, crm, atendimento, localizacao, especialidade, hora)

        medicos.append(medicos)
    

    elif profissao.lower() == "e":
        matricula = input("Digite a matrícula do funcionário: ")
        nome = input("Digite o nome do funcionário: ")
        telefone = input("Digite o número de telefone do funcionário: ")
        email = input("Digite o email do funcionário: ")
        cpf = input("Digite o CPF do funcionário: ")
        rg = input("Digite o RG do funcionário: ")
        coren = input("Digite o COREN do enfermeiro: ")

        
        enfermeiros = Enfermeiros(matricula, nome, telefone, email, cpf, rg, coren)

        enfermeiros.append(enfermeiros)


    else:
        matricula = input("Digite a matrícula do funcionário: ")
        nome = input("Digite o nome do funcionário: ")
        telefone = input("Digite o número de telefone do funcionário: ")
        email = input("Digite o email do funcionário: ")
        cpf = input("Digite o CPF do funcionário: ")
        rg = input("Digite o RG do funcionário: ")

        funcionarios = Funcionario(matricula, nome, telefone, email, cpf, rg)

        funcionarios.append(funcionarios)
    
    resposta = input("Ainda tem mais funcionarios? (S)sim (N)não")



print("Lista de funcionários: ")
for fun in funcionarios:
    print(medicos.nome, "-" ,medicos.telefone, "-", medicos.email, "-", medicos.cpf, "-", medicos.rg, "-", medicos.crm, "-", medicos.atendimento, "-", medicos.localizacao, "-", medicos.especialidade, "-", medicos.hora)

    print("--------------------------------------")

    print(enfermeiros.nome, "-" ,enfermeiros.telefone, "-", enfermeiros.email, "-", enfermeiros.cpf, "-", enfermeiros.rg, "-", enfermeiros.coren)

    print("--------------------------------------")

    print(funcionarios.nome, "-" ,funcionarios.telefone, "-", funcionarios.email, "-", funcionarios.cpf, "-", funcionarios.rg)

    print("--------------------------------------")