print("************")
print("Nome e Senha")
print("************")

from getpass import getpass  #para que a senha não apareça ao ser digitada

nome = "Henrique"
password = "Xlsok=py1"
nova_entrada = "s"

while(nova_entrada == "s"):
    login = (input("Login: ").capitalize())  #'capitalize()' muda a primeira letra da string para maiúscula
    senha = getpass("Senha: ")  #não mostra a senha sendo digitada

    if(login == nome and senha == password):
        print("Entrada permitida...")
        break
    else:
        print("Acesso negado!!!\n")
        
    nova_entrada = input("Tentar novamente? [s/n]: ")
    if(nova_entrada == "n"):
        print("Saindo da tela de acesso...")
