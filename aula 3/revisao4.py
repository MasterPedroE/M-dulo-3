def calcular_media_alunos(alunos):

    soma_notas = 0
    qnt_alunos = len(alunos)

    for aluno in alunos:
        nome = aluno["nome"]
        nota = aluno["nota"]
        soma_notas += nota
        print(f"Nome: {nome}, Notas: {nota}")

    media = soma_notas / qnt_alunos
    return media


alunos =[
    {"nome": "João", "nota":8},
    {"nome": "Maria", "nota":7},
    {"nome": "Pedro", "nota":9},
    {"nome": "Ana", "nota":6}
]

#Chamando a função para calcular a média das alunos
media_notas = calcular_media_alunos(alunos)
print(f"Média da turma: {media_notas}")