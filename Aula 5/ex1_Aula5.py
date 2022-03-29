idade = int(input("Digite a sua idade para a consulta: "))

if idade < 16:
    print(f"Não eleitor, sua idade é abaixo de 16 anos, você tem: {idade}")
elif idade >= 18 or idade == 65:
    print(f"Eleitor obrigatório, sua idade é {idade}")
else:
    print(f"Eleitor facultativo, sua idade é {idade}")

input("Conferindo!!!")