print("************")
print("Nome e Senha")
print("************")
from getpass import getpass     #para que a senha não apareça ao ser digitada

nome = "Henrique"
password = "Xlsok=py1"
while True:
    login = str(input("Login: ").lower())   #'capitalize()' muda a primeira letra da string para maiúscula
    senha = getpass("Senha: ")     #não mostra a senha sendo digitada
    if(login.lower() == nome.lower() and senha == password):
        print("Entrada permitida...")
        break
    else:
        print("Acesso negado!!!\n")
    nova_entrada = input("Tentar novamente? [s/n]: ")
    if(nova_entrada == "n"):
        print("Saindo da tela de acesso...")
        break

