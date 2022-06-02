faturamento = float(input("Digite o faturamento: R$ "))
custo = float(input("Digite o custo: R$ "))
lucro = faturamento - custo
lucro = f"R$ {lucro:_.2f}"
print(lucro.replace('.', ',').replace('_', "."))