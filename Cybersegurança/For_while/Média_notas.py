print("*********************************")
print("Exercícios Python - Intermediário")
print("*********************************")
"""
for i in range(3):
    nota = float(input(f"Informe a nota da {i + 1}ª prova: "))
"""

n1 = float(input("Nota da 1ª prova: "))
n2 = float(input("Nota da 2ª prova: "))
n3 = float(input("Nota da 3ª prova: "))

media = ((n1 + n2 + n3) / 3)
if (media >= 7):
    print(f"Aluno aprovado! Média {media:.2f}")
else:
    print(f"Aluno reprovado... Média {media:.2f}")


