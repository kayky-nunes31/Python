#Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de
#segundo grau, apresentando: as duas raízes, quando for possível efetuar o cálculo
#(delta positivo ou zero); a mensagem "Não há raízes reais", se não for possível fazer o
#cálculo (delta negativo); e a mensagem "Não é equação do segundo grau", se o valor
#de a for igual a zero.

ax = float(input("Digite o valor de A:"))
bx = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))

# Operação Delta
delta = (bx**2) - 4 * ax * c

if delta < 0:
    print("Não é equação do segundo grau")
elif delta > 0:
    print("Não há raízes reais")

print(f"O valor de Delta é: {delta}")

input("Conferindo")