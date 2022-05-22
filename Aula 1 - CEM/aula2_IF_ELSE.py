nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f"Aluno(a) Aprovado(a)!!! Com a nota: {media}")
elif media == 10:
    print(f"PARABÉNSSS Você fechou com {media}")
else:
    print(f"Aluno(a) Reprovado(a), sua media foi: {media}")

input("Conferindo!!!")