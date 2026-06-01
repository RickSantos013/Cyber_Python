print("*********************************")
print("Exercícios Python - Intermediário")
print("*********************************")

contador = 0
for i in range(1,51):
    if (i % 2 == 0):
        contador = contador + 1
        print(i)
print(f"O total de números pares de 1 a 50 é: {contador}")
