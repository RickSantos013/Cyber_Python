import random

def imprime_abertura():
     print("✯✯✯✯✯✯✯✯✯✯✯✯✯")
     print("Jogo da Forca")
     print("✯✯✯✯✯✯✯✯✯✯✯✯✯")

def escolhe_palavra_secreta ():
    arquivo = open("frutas.txt", "r")       #abre o arquivo e faz somente a leitura
    palavras = []

    for linha in arquivo:            #lê cada linha do arquivo
        linha = linha.strip()        #remove espaços e '\n' das palavras
        palavras.append(linha)       #adiciona cada linha lida do arquivo à lista de palavras

    arquivo.close()

    numero = random.randrange(0,len(palavras))          #gera um número aleatório de 0 até o tamanho da lista de palavras do arquivo, que é o índice de cada fruta
    palavra_secreta = palavras[numero].upper()          #recebe o índice referente à palavra da lista e transforma em MAIÚSCULO
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def palpite():
    chute = input("Qual letra? ")        
    chute = chute.strip().upper()           #strip - remove espaços antes ou depois da palavra
    return chute 

def jogar():

    imprime_abertura()    
    palavra_secreta = escolhe_palavra_secreta()    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    enforcou = False
    acertou = False
    erros = 0
    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = palpite()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):              
                    letras_acertadas[index] = letra 
                index = index + 1
        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)    

    if (acertou):
        print("Você acertou a palavra")
    else:
        print("Você perdeu...")

if(__name__ == "__main__"):
    jogar()