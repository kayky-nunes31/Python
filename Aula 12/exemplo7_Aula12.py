import trigonometria

catO = float(input("Digite o cateto oposto: "))
catA = float(input("Digite o cateto adjascente: "))

print(f"Seno = {trigonometria.seno(catO, catA)}")
print(f"Cosseno = {trigonometria.cosseno(catO, catA)}")
print(f"Tangente = {trigonometria.tangente(catO, catA)}")