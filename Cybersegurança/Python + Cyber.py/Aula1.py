"""#Biblioteca os
import os
print("Diretório atual: ", os.getcwd())  #diretório onde python está sendo executado

arquivos = os.listdir()
print("Arquivos e pastas aqui: ", arquivos)

#Biblioteca subprocess
#1. Executar comando e capturar a saída
#Linux: "ls" "-l"
import subprocess
resultado = subprocess.run(['cmd', '/c', 'dir'], capture_output=True, text=True)
print("Saída do comando: ", resultado.stdout)

#2. Verificas status
comando = subprocess.run(["ping", "-n", "4", "google.com"], capture_output=True)
if comando.returncode == 0:
    print("Conexão ativa!")
else:
    print("Sem internet...")"""

import os
import time

#caminho atual (pasta onde o script está)
caminho = "."
hoje = time.strftime("%y-%m-%d") #captura da data de hoje (formato: ano-mês-dia)

with open("log.txt", "w") as log: #cria ou sobrescreve o arquivo de log
    for arquivo in os.listdir(caminho): #percorre todos os arquivos da pasta
        if arquivo.endswith(".py"): #verifica se o arquivo termina com (.py)
            modificado = time.strftime("%y-%m-%d", time.localtime(os.path.getmtime(arquivo))) #captura a data da últime verificaçao
            if modificado == hoje: #compara com a data de hoje
                log.write(f"{arquivo} foi modificado hoje\n")

