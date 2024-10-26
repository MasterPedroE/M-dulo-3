pessoas =[
    {"nome": "João", "idade":25},
    {"nome": "Maria", "idade":30},
    {"nome": "Pedro", "idade":28},
    {"nome": "Ana", "idade":22}
]

#acessando os elementos da lista
for pessoas in pessoas:
    nome = pessoas["nome"]
    idade = pessoas["idade"]
    print(f"Nome: {nome}, idade: {idade}")