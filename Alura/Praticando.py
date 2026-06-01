print("*****************")
print("Praticando Python")
print("*****************")

"""
#04 
maca = 0
banana = 0
maca = int(input("Informe a quantidade de maças vendidas no mês: "))
banana = int(input("Informe a quantidade de bananas vendidas no mês: "))
if(maca > banana):
    print("As maças tiveram mais vendas.")
elif(maca == banana):
    print("Houve um empate nas vendas de maças e bananas")
else:
    print("As bananas venderam mais que as maças.") 

#05
A,B,C,total = 0,0,0,0
A = int(input("Informe os dias para a atividade A: "))
B = int(input("Informe os dias para a atividade B: "))
C = int(input("Informe os dias para a atividade C: "))
total = (A+B+C)
if(A < 0 or B < 0 or C < 0):
    print("Os dias não podem ser negativos...")    
else:
    print(f"O total das três atividades será de {total} dias") 

#06
temperatura = int(input("Informe a temperatura atual da sala: "))
if(temperatura > 25):
    print("ALERTA!! Temperatura acima do limite permitido.") 

#07 - IMC
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura**2)
print(f"Seu IMC é {imc:.2f}")
if(imc < 18.5):
    print("Você está abaixo do peso")
elif(imc >= 18.5 and imc < 25):
    print("Você está no peso ideal")
else:
    print("Você está acima do peso") 

#08
gastos = float(input("Informe o total dos seus gastos mensais (R$): "))
if(gastos >= 3000):
    print(f"ATENÇÃO! Você ultrapassou seu limite de orçamento.") 

#09 - CONTROLE DE HORAS | COMPARAÇÃO DE HORAS
from datetime import datetime, time
hora = (input("Informe a hora atual (HH:MM): "))
horario = datetime.strptime(hora, "%H:%M").time()   #converte a string de 'hora' para um valor que o python entende como hh:mm
if (time(8,0) <= horario <= time(21,0)):   #p/ fazer comparações, tem que usar objetos 'time'
    print("Acesso permitido!")
else:
    print("Acesso negado...") 

#10 - NOTAS DE ESCOLA
n1 = float(input("Nota da 1a prova: "))
n2 = float(input("Nota da 2a prova: "))
n3 = float(input("Nota da 3a prova: "))
media = (n1+n2+n3) / 3
print(f"Média do aluno: {media:.2f}")
if(media >= 7):
    print("APROVADO :)")
elif(media >= 5 and media < 7):
    print("RECUPERAÇÃO --'")
else:
    print("REPROVADO...") 

#11 - PEDÁGIO
distancia = int(input("Informe a distância percorrida (km): "))
if(distancia > 0 and distancia <= 100):
    print("Valor do pedágio: R$10")
elif(distancia >= 100 and distancia <= 200):
    print("Valor do pedágio: R$20")
else:
    print("Valor do pedágio: R$30")  

#12 - Número PAR
numero = int(input("Digite um número inteiro: "))
if(numero % 2 == 0):
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")

#13 - 
renda = float(input("Informe sua renda mensal (R$): "))
parcela = float(input("Informe o valor da parcela desejada (R$): "))
condicao = renda * 0.3
porcentagem = (parcela * 100) / renda
if(parcela > condicao):
    print(f"Empréstimo negado: parcela {porcentagem:.2f}% da renda.")
else:
    print(f"Empréstimo aprovado! parcela {porcentagem:.2f}% da renda.")  

                #FOR e WHILE
#04 - percorra a lista de nomes e exiba cada cliente.
clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]
for i in clientes:
    print(i) 

#05
contador = 0
while contador < 10:
    print("Processando dados...")
    contador += 1 

#06 - 
contador = 0
while contador < 5:
    print("Bem-vindo ao Buscante!")
    contador += 1 

#07 - 
valores = [10,20,30,40,50]
total = 0
for i in valores:
    total += i
print(f"Soma total das receitas: {total}") 

#08 - TROCA UM ITEM DA LISTA
projetos = ["Website", "Jogo", "Análise de Dados", None, "Aplicativo móvel"]
for i in range(len(projetos)):
    if(projetos[i] == None):
        projetos[i] = "Projeto ausente"
for i in projetos:
    print(i) 

#09
import time
livros = ["1984", "Dom Casmurro", "O Pequeno Principe", "O Hobbit", "Orgulho e Preconceito"]
procura = str(input("Qual livro procura: ")).lower().strip()
print("Pesquisando...")
time.sleep(1)
for posicao, livro in enumerate(livros):    #percorre a lista, pegando ao mesmo tempo a posição
    if(procura == livro.lower()):
        print(f"Livro encontrado: {livro} na posição {posicao}")
        break
else:
    print("Livro não encontrado!") 

#10 - CONTROLE DE ESTOQUE
qtde = int(input("Informe a quantidade de livros no estoque: "))
while(qtde > 0):
    qtde -= 1
    print(f"Venda realizada! Estoque restante {qtde}")
print("Estoque esgotado!") 

#11 - CONTAGEM REGRESSIVA
for i in range(10, 0, -1):
    if(i % 2 == 0):
        print(f"Faltam apenas {i} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua: {i} segundos restantes.")
print("Aproveite a promoção agora!") 

#12 -
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]
for posicao, livro in enumerate(livros):
    if(livro["estoque"] > 0):
        print(f"Livro disponível: {livro['nome']} na posição {posicao + 1}") 

#13 - VALIDAÇÃO DE LOGIN
from getpass import getpass     #getpass não funciona no pycharm, somente no vscode
while True:
    usuario = str(input("Digite seu nome de usuário: "))
    senha = getpass("Digite sua senha: ")
    if(len(usuario) < 5):
        print("O nome de usuário deve ter pelo menos 5 caracteres")
        continue
    if(len(senha) < 8):
        print("A senha deve ter pelo menos 8 caracteres")
        continue
    print("Cadastro realizado com sucesso!")
    break   

        #FUNÇÕES
def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

nascimento = int(input("Digite o ano do seu nascimento: "))
atual = int(input("Digite o ano atual: "))
idade = calcular_idade(nascimento, atual)
print(f"A idade é {idade} anos.") 

#05 - CONTADOR DE CARACTERES
def calcular_caracteres(palavra):
    return len(palavra)
palavra = str(input("Digite uma palavra: "))
print(f"A palavra '{palavra}' tem {calcular_caracteres(palavra)} caracteres.") 

#06 - SAUDAÇÃO PERSONALIZADA A PARTIR DO HORÁRIO
def saudacao(hora):
    if(hora < 12):
        return ("Bom dia!")
    elif(hora < 18):
        return ("Boa tarde!")
    else:
        return ("Boa noite!")
hora_atual = int(input("Informe a hora atual (0-23h): "))
print(saudacao(hora_atual)) """

#08 - TOTAL DE VENDAS
def soma():
    soma = (a+b)
    return soma
a = int(input("Digite o valor da primeira venda: "))
b = int(input("Digite o valor da segunda venda: "))
print(f"A soma total das vendas, foi de {soma()} vendas") 





   





    

