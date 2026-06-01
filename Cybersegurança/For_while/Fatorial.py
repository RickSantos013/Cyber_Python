print("****************************")
print("Exercícios Python - Avançado")
print("****************************")

""
num = int(input("Digite um número e veja seu fatorial: "))
fatorial = 1

for i in range(1, num + 1):
    fatorial = i * fatorial
print(f"{num}! é igual a {fatorial}")

"""
num = int(input("Digite um número e veja seu fatorial: "))
contador = 1
fatorial = 1

while(contador <= num):
    fatorial = fatorial * contador
    contador = contador + 1
print(fatorial)
"""