#Criando arquivo com conteúdo
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá mundo! Bem-vindo ao curso de python")

with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#lendo linha por linha
with open("exemplo.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())