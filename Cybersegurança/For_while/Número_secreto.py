print("*********************************")
print("Exercícios Python - Intermediário")
print("*********************************")

num_secreto = 42
palpite = 0

while(palpite != num_secreto):  
    palpite = int(input("Qual é o número secreto? "))  
    if(palpite > num_secreto):
        print("O palpite foi maior que o número secreto...")
    elif (palpite < num_secreto):
        print("O palpite foi menor que o número secreto...")
    else:
        print("Parabéns! Você acertou o número secreto!")
