salario = float(input("Digite seu salário desse mês"))
imposto = (salario *11) /100
inss = (salario*8) / 100
sindicato = (salario*5) / 100

roubo = imposto + inss + sindicato
liquido = salario - roubo

print("Seu salário bruto é de R$:",salario)
print("R$", imposto, "Serão tirado por impostos")
print("R$",inss, "Vão para o INSS")
print("R$",sindicato, "Irão ir para o sindicato")

print("No total, foram descontados R$",roubo, "do seu salário")
print("Lhe restando R$",liquido)