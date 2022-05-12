valores = []
par = 0
impar = 0

while True:
    num = int(input("Digite um número: "))
    continuar = input("Deseja continuar? ")
    if num > 0:
        valores.append(num)
        par = par + 1
    elif num < 0:
        valores.append(num)
        impar = impar + 1
    if continuar in "Nn":
        break

print(f"Esses é a quantidade de números pares: {par}")
print(f"Esses é a quantidade de números pares: {impar}")