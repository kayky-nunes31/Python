ax = float(input("Digite o valor de A: "))
bx = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

print(f"A sua esquação de 2º Grau é: {ax}x² + {bx}x + {c}")


# Operação Delta
delta = (bx**2) - 4 * ax * c

print(f"O valor de Delta é: {delta}")


# Operações dos X's
x1 = (-bx + delta ** (1 / 2)) / (2 * ax)
x2 = (-bx - delta ** (1 / 2)) / (2 * ax)

print(f"O valor de x1 é: {x1}; E o valor de x2 é: {x2}")

input("Conferindo")