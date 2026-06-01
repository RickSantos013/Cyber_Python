print("****************************")
print("Exercícios Práticos - Python")
print("****************************")

"""
#Exercício - Conversão real > dólar
num = float(input("Valor a ser convertido(R$): "))
cambio = num / 5.01 
print(f"R${num} é = US${cambio:.2f}")

#Exercício - Qtde de tinta/m²
l = float(input("Largura da parede(m): "))
a = float(input("Altura da parede(m): "))
area = l * a
tinta = area / 2
print(f"Tinta necessária: {tinta}L")

#Exercício - Desconto variável
preco = float(input("Informe o preço do produto(R$): "))
desconto = float(input("Desconto(%): "))
desconto2 = preco * (desconto/100)
novo_preco = preco - desconto2
print(f"Valor a pagar: R${novo_preco}")

#Exercício - Aumento de salário
salario = int(input("Informe seu salário (R$): "))
aumento = salario + (salario * (15/100))
print(f"Seu novo salário será de R${aumento}")

#Exercício - Celsius para Fahrenheit
c = int(input("Informe a temperatura(°C): "))
f = 1.8 * c + 32
print(f"{c}°C é igual a {f}°F")

#Exercício - Aluguel de carro
dias = int(input("Informe quantos dias utilizou o carro: "))
km = int(input("Informe quantos km percorridos: "))
preco = 60 * dias + 0.15 * km
print(f"Valor a ser pago é de R${preco}")

#Exercício - Escolhe algo dentro de uma lista
import random
lista = []
for i in range(3):
    lista.append(input(f"{i+1}° aluno: "))
sorteado = random.choice(lista) #faz a escolha aleatória dentro da lista
print(f"O aluno escolhido foi: {sorteado}")

#Exercício - Embaralha uma lista com nomes 
import random
lista = []
for i in range(4):
    lista.append(input(f"Digite o nome do {i+1}° aluno: "))
    random.shuffle(lista) #embaralha a lista, mas não retorna nada
print(lista)

#Exercício 22 - 
nome = str(input("Digite o seu nome completo: "))
maius = nome.upper()
minus = nome.lower()
total_letras = len(nome.strip()) #'len' mostra o tamanho da string - strip() remove espaços antes e depois
sep = nome.split() #separa a string dentro de uma lista
print(maius, minus, total_letras)
print("A qtde de letras no 1° nome é: ", len(sep[0]))

#Exercício - 
nome = str(input("Digite o seu nome completo: ")).strip()
if ("silva" in nome.lower() or 'silva' in nome.upper()):
    print("Tem 'Silva' no seu nome!")
else:
    print("Não tem 'Silva' no seu nome...")
n = str(input("Digite seu nome completo: ")).strip()
nome = n.split()
print(nome)

#Exercício 28 - Adivinha número com delay
import random
import time
num_sorteado = random.randint(1,5)  #gera número aleatório entre 1 e 5(inclusive)
num = int(input("Digite um número entre 0 e 5: "))
if (num == num_sorteado):
    print("PROCESSANDO...")
    time.sleep(2)
    print("Parabéns, você acertou!")
else:
    print("PROCESSANDO...")
    time.sleep(2)
    print("Você perdeu!") 

#Exercício 29 - Multa por velocidade
velocidade = int(input("Qual a velocidade atual do carro: "))
if(velocidade > 80):
    multa = (velocidade - 80) * 7
    print(f"Você excedeu o limite permitido de 80km/h\nVocê foi multado e pagará R${multa}")
else:
    print("Você está no limite da via")
 
#Exercício 30 - Par ou ímpar
num = int(input("Digite um número: "))
if (num % 2 == 0):
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")

#Exercício 31 - Preço pago/km
distancia = int(input("Qual a distância da viagem: "))
if(distancia <= 200):
    preco = distancia * 0.5
    print(f"Você pagará R${preco}")
elif(distancia > 200):
    preco = distancia * 0.45
    print(f"Você pagará R${preco}") 

#Exercício 33 - Maior e menor número dentro de uma lista
lista = []
for i in range (3):
    num = int(input("Digite um número: "))
    lista.append(num)
print(f"O maior número é: {max(lista)}")
print(f"O menor número é: {min(lista)}")

#Exercício 34 - Aumento de salário 10 e 15%
salario = int(input("Informe o seu salário: "))
if(salario > 1250):
    aumento = salario * 0.1
    novo_salario = salario + aumento
    print(f"Você terá um aumento de R${aumento} e receberá R${novo_salario}")
else:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"Você terá um aumento de R${aumento} e receberá R${novo_salario}")

#Exercício 46 - Contagem regressiva com delay de 1s
import time
print("Contagem regressiva...")
try:
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
except KeyboardInterrupt:
    print("Programa interrompido --'")

#Exercício 47 - Pares de 1 a 50
print("Números pares de 1 a 50: ")
for i in range (0, 50):
    if(i % 2 == 0):
        print(i) 

#Exercício 48 - ímpares e múltiplos de 3 até 500
soma = 0
for i in range(1, 500):
    if(i % 2 == 1 and i % 3 == 0):
        soma += i
        print(i)
print(f"A soma desses números ímpares é {soma}")

#Exerício 49 - Tabuada usando for
num = int(input("Digite um número e veja sua tabuada: "))
for i in range (1, 11):
    multiplicacao = num * i
    print(f"{num} x {i} = {multiplicacao}")

#Exercício 50 - lê 6 números inteiros e soma somente os pares
soma = 0
for i in range (0, 6):
    num = int(input("Digite um número inteiro: "))
    if(num % 2 == 0):
        soma += num
print(f"Soma dos números pares informados: {soma}") 

#Exercício 57 - MASCULINO - FEMININO
while True:
    sexo = str(input("Qual seu sexo? [M/F]: ")).upper()
    if(sexo == "M"):
        print(f"Você é do sexo masculino.")
        break
    elif(sexo == "F"):
        print("Você é do sexo feminino.")
        break
    else:
        print("Entrada inválida... Digite novamente!") 

#Exercício 54 -
lista = []
ano_atual = 2026
maior, menor = 0,0
for i in range (1,4):
    ano = int(input("Digite o ano do seu nascimento: "))
    lista.append(ano)
    confere = ano_atual - ano
    if(confere >= 18):
        maior += 1
    else:
        menor += 1
print(lista)
print(f"Pessoas +18: {maior}")
print(f"Pessoas menores de idade: {menor}") 

#Exercício 55 -
lista = []
for i in range(1,6):
    peso = float(input("Informe o seu peso (kg): "))
    lista.append(peso)
print(f"O maior peso é: {max(lista)}kg")
print(f"O menor peso é: {min(lista)}kg") """

"""#Exercício 58 -
import random
tentativas = 0
num = random.randint(1,10)
print("Tente adivinhar um número entre 1 e 10")
while True:
    palpite = int(input("Digite um número: "))
    if(palpite == num):
        print(f"Você acertou o número secreto: {num}")
        break
    elif(palpite != num):
        print("Você errou! Continue tentando...")
        tentativas += 1
print(f"Você fez {tentativas} tentativas até acertar") 

#Exercício 59 -
import time
while True:
    print("--- MENU Matemático ---\n [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos números\n [5] Sair")
    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite um número inteiro: "))
    opcao = int(input("Escolha uma opção: "))
    if(opcao == 1):
        print("Opção escolhida: Somar")
        soma = num1 + num2
        print(f"A soma dos números digitados é: {soma}")
    elif(opcao == 2):
        print("Opção escolhida: Multiplicar")
        multiplica = num1 * num2
        print(f"A multiplicação dos números digitados é: {multiplica}")
    elif(opcao == 3):
        print("Opção escolhida: Maior")
        if(num1 > num2):
            maior = num1
            print(f"O maior número entre os digitados é: {maior}")
        elif(num1 == num2):
            print("Os números digitados, são iguais")
        else:
            maior = num2
            print(f"O maior número entre os digitados é: {maior}")
    elif(opcao == 4):
        print("Opção escolhida: Novos números")
        continue
    elif(opcao == 5):
        print("Opção escolhida: Sair")
        print("Saindo do programa...")
        time.sleep(1)
        break
    else:
        print("Opção inválida! Digite novamente!")
    continua = str(input("Deseja escolher outra opção? [s/n]: "))
    if(continua == "n"):
        print("Saindo do programa...")
        break 

#Exercício 63 - Sequência de Fibonacci - FIZ COM AJUDA
qtde = int(input("Digite um número inteiro: "))
n1 = 0
n2 = 1
cont = 0
while(cont < qtde):
    print(n1)
    proximo = n1 + n2
    n1 = n2
    n2 = proximo
    cont += 1 

#Exercício 64 -
cont = 0
soma = 0
while True:
    try:
        num = int(input("Digite um número inteiro: (p/ sair: 999): "))
        if(num == ""):
            continue
        cont += 1
        soma += num
        if(num == 999):
            print("Finalizando o programa...")
            break
    except ValueError:
        print("Valor inválido! Digite apenas números inteiros.")
print(f"O total de números digitados foi: {cont - 1}")
print(f"A soma dos números digitados foi: {soma - 999}") 

#Exercício 65 -
qtde = 0
soma = 0
lista = []
while True:
    try:
        num = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Digite apenas números inteiros.")
        continue
    lista.append(num)
    qtde += 1
    soma += num
    media = soma/qtde
    pergunta = str(input("Deseja continuar? [s/n]: ")).strip().lower()
    while(pergunta not in ["s", "n"]):
        pergunta = input("Resposta inválida! Digite [s/n]: ").strip().lower()
    if(pergunta == "n"):
        print("Finalizando o programa...")
        break
print(f"A média dos números digitados é: {media:.2f}")
print(f"O maior número digitado foi: {max(lista)}")
print(f"O menor número digitado foi: {min(lista)}")  """

""" #Exercício 74 - Gera números aleatórios, coloca em tupla e mostra o maior e o menor
import random
tupla = ()
for i in range(0, 5):
    num = random.randint(1,20)
    tupla = (num,) + tupla        #(num, ) adiciona novo valor dentro da tupla
    print(num)
print(f"O menor número é {min(tupla)}")
print(f"O maior número é {max(tupla)}")  

#Exercício 78 - 
lista = []
for i in range(0, 5):
    lista.append(int(input("Digite um número: ")))
print(f"O menor número da lista é {min(lista)}")
print(f"O maior número da lista é {max(lista)}") 

#Exercício 79 -
lista = []
resposta = "s"
while(resposta == "s"):
    num = (int(input("Digite um valor: ")))
    if(num not in lista):
        lista.append(num)
    else:
        print("Valor duplicado")
    resposta = str(input("Deseja continuar? [s/n] ")).lower()
    if(resposta == "n"):
        break
lista.sort()
print(lista) 

#Exercício 80 - FIZ COM AJUDA
lista = []
pos = 0
for i in range (0, 3):
    num = (int(input("Digite um número: ")))
    if (i == 0 or num >lista[-1]):  #lista[-1] pega o último número da lista
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if(num <= lista[pos]):
                lista.insert(pos,num)
                break
            pos += 1
print(lista) 

#Exercício 81 -
lista = []
cont = 1
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    if(num == 5):
        posicao = len(lista) - 1   
    pergunta = str(input("Quer continuar? [s/n] ")).lower()
    if(pergunta == 'n'):
        break
    cont += 1
if(5 in lista):
    print(f"O número 5 está na lista na posição {posicao}")
else:
    print("O número 5 não está na lista")
print(f"Total de números digitados: {cont}")
lista.sort(reverse=True)
print(f"Lista em ordem decrescente: {lista}") 

#Exercício 82 -
lista = []
pares = []
impares = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    if(num % 2 == 0):
        pares.append(num)
    else:
        impares.append(num)
    pergunta = str(input("Quer continuar? [s/n] ")).lower()
    if(pergunta == 'n'):
        break
print(lista)
print(f"Lista dos pares: {pares}")
print(f"Lista dos ímpares: {impares}") 

   #LISTAS COMPOSTAS
galera = list()
dado = list()
maior, menor = 0,0
print("Informe os dados a seguir: ")
for i in range(0,2):
    dado.append(str(input("Nome: ")))  #nome na posição 0
    dado.append(int(input("Idade: ")))   #idade na posição 1
    dado.append(str(input("Sexo: ")))  #sexo na posição 2
    galera.append(dado[:])  #faz uma cópia dos valores da lista 'dado' para a lista 'galera'
    dado.clear()    #limpa a lista, para serem incluídos novos valores
for i in galera:
    if(i[1] >= 18):
        maior += 1
    else:
        menor += 1
print(galera)
print(f"Há {maior} maiores de idade")
print(f"Há {menor} menores de idade") 

#Exercício 84 -
lista1 = list()
lista2 = list()
print("Informe os dados a seguir: ")
while True:
    lista2.append(str(input("Nome: ")))
    lista2.append(int(input("Peso(kg): ")))
    lista1.append(lista2[:])    #copia os dados da lista2 para a lista1
    lista2.clear()      #limpa a lista2
    pergunta = str(input("Acrescentar mais dados? [s/n] ")).lower()
    if(pergunta == "n"):
        break
print(lista1) 

#Exercício 85 -
lista = [[],[]]       #lista dentro de lista
for i in range(0,7):
    num = int(input("Digite um número inteiro: "))
    if(num % 2 == 0):
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()    #coloca em ordem crescente
lista[1].sort()
print(f"Lista completa: {lista}")
print(f"Lista dos números pares: {lista[0]}")   #sorted(lista[0]) - coloca em ordem crescente tbm
print(f"Lista dos números ímpares: {lista[1]}")  """

#Exercício 88 -
import random
lista = []
lista2 = []
print("-- MEGA SENA --")
jogos = int(input("Deseja fazer quantos jogos?: "))
for i in range(0,jogos):
    for j in range(0,6):
        sorteio = random.randint(1,60)
        if(sorteio not in lista):
            lista.append(sorteio)
    lista2.append(lista[:])    #copia a 'lista2' para a 'lista'
    lista.clear()              #apaga os valores, para novos serem adicionados
for a, b in enumerate(lista2):
    print(f"Jogo {a}: {b}")






















    







    




