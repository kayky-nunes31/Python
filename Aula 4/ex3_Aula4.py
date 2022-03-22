compra = float(input("Qual foi o valor da sua compra: "))

if compra >= 200:
    porcentagem = compra * 0.2
    print(f"Você obteve um desconto na sua compra de: R${porcentagem} reais")
else:
    print(f"Esse é o valor da sua compra: {compra}")

input("Conferindo")