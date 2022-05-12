lista_dia = []
lista_tempo = []
soma = 0

for i in range(2):
    dia = input("Digite qual o dia da semana: ")
    chuva = float(input(f"Informe o volume da chuva de {dia}: "))

    if dia == "quarta" or dia == "Quarta":
        soma = soma + 1
    if chuva > 0:
        total = chuva + chuva

media = total / soma
print(f"Essa é a média do volume de chuva às Quartas-feiras: {media}")
print(f"Esse é o tatal do volume das chuvas {total}")

input("Conferindo")