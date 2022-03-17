#Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.

anos = int(input("Digite a sua idade aqui: "))
meses = int(input("Digite a sua idade em meses aqui: "))
dias = int(input("Digite a sua idade em dias aqui: "))

anos_dias = anos * 365
meses_dias = meses * 30

print(f"Esse são seus anos de idade convertidos em dias: {anos_dias}")
print(f"Esse são seus meses de idade convertidos em dias: {meses_dias}")
print(f"Esse são todos os seus dias de vida {dias}")

input("Conferindo")