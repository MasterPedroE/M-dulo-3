nivel = input("Diga o seu nível")
horas_aula = float(input("Agora a quantidade de horas extras"))


if nivel == "1":
    salbase = 56 * horas_aula
elif nivel == "2":
    salbase = 66 * horas_aula
else:
    print("Esse nível não existe")

dsr = salbase * 0.15
salario = salbase + dsr

print(f"o salario do professor é: R${salario:.2f}")