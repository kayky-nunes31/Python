nota1 = float(input("Digite a nota da mensal: "))
nota2 = float(input("Digite a nota da bimestral: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Aluno(a) Aprovado(a) com a nota: ", media)
else:
    print("Aluno(a) Reprovado(a) com a nota: ", media)

input("Confere ai meu chapa :)")