print("************")
print("Try / Except")
print("************")

#Peça um número inteiro ao usuário.
#Se ele digitar algo inválido, mostre uma mensagem de erro.
"""
try:
    num = int(input("Digite um número inteiro: "))   
    print(f"Você digitou o número {num}")    
except ValueError:
    print("Você digitou algo que não é um número ou um não é um número inteiro!")
except ZeroDivisionError:
    print("Não pode dividir por zero!")
"""
#Peça dois números e faça a divisão entre eles.
#Trate erro de número inválido
#Trate divisão por zero
"""
try:
    num1 = int(input("Digite o 1º número: "))    
    num2 = int(input("Digite o 2º número: "))
    divisao = (num1/num2)
    print(f"A divisão de {num1} por {num2} é = {divisao}")
except ValueError:
    print("Você digitou algo que não é um número!")
except ZeroDivisionError:
    print("Não pode dividir por zero!")
"""

#Peça um número inteiro até o usuário digitar corretamente.
try:
    while True:
        num = int(input("Digite um número inteiro: "))
        print(f"Você digitou o número {num}")
        break
except ValueError:
    print("Você digitou um número que não é inteiro!")


