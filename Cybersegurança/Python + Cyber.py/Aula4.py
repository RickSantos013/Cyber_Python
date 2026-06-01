import subprocess

comando = subprocess.run(["ping", "-n", "4", "google.com.br"], capture_output=True, text=True)

#cria arquivo de log e salva o resultado
with open("log-rede.txt", "w") as log:
    log.write(comando.stdout)
print("Informações de rede salvas no 'log-rede.txt'")

#lê arquivos de log
with open("log-rede.txt", "r") as log:
    conteudo = log.read()
print("Conteúdo do log: \n")
print(conteudo)

