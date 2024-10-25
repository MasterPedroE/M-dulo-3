def calcular_salario_professor(nivel, horas_aula):
    if nivel == 1:
        salbase = 56 * horas_aula
    elif nivel == 2:
        salbase = 66 * horas_aula
    else:
        print("Nível Inexistente!")
        return 0

    dsr = salbase * 0.15
    salario = salbase + dsr
    return salario

# CORPO DO PROGRAMA
nivel = int(input("Digite o nível do professor (1 ou 2): "))
horas_aula = float(input("Digite a quantidade de horas de aula dadas no mês: "))


salario = calcular_salario_professor(nivel, horas_aula)

if salario > 0:
    print(f"O salário do professor é: R${salario:.2f}")