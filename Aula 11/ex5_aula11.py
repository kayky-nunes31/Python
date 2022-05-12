lista_alunos = []
lista_notas = []
lista_curso = []

qtd_curso = 0
qtd_curso2 = 0

qtd_notas = 0
soma = 0

for i in range(10):
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota do {nome}: "))
    curso = input(f"Digite o curso do(a) {nome} (ccp ou ads):  ")
    lista_alunos.append(nome)
    lista_notas.append(nota)
    lista_curso.append(curso)

    if curso == "ads":
        qtd_curso = qtd_curso + 1
    elif curso == "ccp":
        qtd_curso2 = qtd_curso2 + 1

for n in lista_notas:
    soma += n
    if nota > 6:
        qtd_notas = qtd_notas + 1

media = soma / 10

print(f"Essa é a quantidade de alunos do curso de ads: {qtd_curso}")
print(f"Essa é a média de notas dos alunos em geral: {media}")
print(f"Esse é o número de alunos acima da média: {qtd_notas}")