import random               #importa função que gera números decimais aleatórios

def jogar():
    print("******************")
    print("Jogo da Adivinhação")
    print("******************")

    num_secreto = random.randrange(0,101)     #gera número aleatório de 1 a 100
    tentativas = 0
    pontos = 1000 

    print("DIFICULDADE")
    print("[1] Fácil [2] Médio [3] Difícil")
    nivel = int(input("Qual dificuldade você escolhe: "))

    if (nivel == 1):         #inteiro, sem aspas | string, dentro de aspas
        tentativas = 10
    elif (nivel == 2):
        tentativas = 5
    else:
        tentativas = 3

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))  #interpolação de strings
        chute = int(input("Digite um número entre 1 e 100: "))
        if(chute < 1 or chute > 100):
            print("Digite somente números positivos!")
            continue        
        maior = chute > num_secreto
        menor = chute < num_secreto    

        pontos_perdidos = abs(num_secreto - chute)
        pontos = pontos - pontos_perdidos
        if(maior):
            print("O número secreto é menor que {}".format(chute))
        elif(menor):
            print("O número secreto é maior que {}".format(chute))
        else:
            print("\n")
            print("✯✯✯✯✯✯✯✯")
            print("Você acertou e fez {} pontos!".format(pontos))
            break    

if(__name__ == "__main__"):
    jogar()