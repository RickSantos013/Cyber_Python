#Biblioteca OS
#Interação direta com o sistema de arquivos e ambientes

import os

os.makedirs("Exemplo_diretório", exist_ok=True)
print("Diretório criado")

#Lista arquivos no diretório atual
arquivos = os.listdir(".")
print("Arquivos no diretório atual: ")
print(arquivos)

#Renomear o diretório atual
os.rename("Exemplo_diretório", "Novo diretório")
print("Diretório renomeado")

#Remover o diretório
os.rmdir("Novo diretório")
print("Diretório removido")
