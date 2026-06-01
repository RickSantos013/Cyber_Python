import subprocess

"""#PING
                         #["comando", "-n(windows) | -c(linux)", "qtde de pacotes desejados", "endereço desejado"]
comando = subprocess.run(["ping", "-n", "4", "google.com"], capture_output=True, text=True)
print("Saída: ", comando.stdout) #mostra o retorno do ping
#print("Código de retorno: ", comando.returncode) #0 - tudo ok; != 0 - erro
if comando.returncode == 0:
    print("Conexão OK!")
else:
    print("Falha de conexão...")

#NETSTAT
                        #["comando", "-a(todas conexões e portas) -n(mostra de forma numérica)"]
comando = subprocess.run(["netstat", "-an"], capture_output = True, text=True)
if comando.returncode == 0:
    print("Conexões de rede encontradas: ")
    print(comando.stdout)
else:
    print("Erro ao executar netstat")

#FUNÇÃO REUTILIZÁVEL
def executar_comando(comando: list):
    resultado = subprocess.run(comando, capture_output=True, text=True)
    if resultado.returncode == 0:
        return resultado.stdout
    else:
        return (f"Erro ao executar {comando}")    
    
saida_ping = executar_comando(["ping", "-n", "4", "google.com"])
print(saida_ping)
saida_netstat = executar_comando(["netstat", "-an"])
print(saida_netstat)

with open("log_netstat.txt", "w") as log:
    log.write(executar_comando(["netstat", "-an"]))

#WHOAMI
comando = subprocess.run(["whoami"], capture_output=True, text=True)
if comando.returncode == 0:
    print("Comando 'whoami' executado com sucesso: ")
    print(comando.stdout)
else:
    print("Comando não executado...")

#IPCONFIG
rede = subprocess.run(["ipconfig"], capture_output=True, text=True)
if rede.returncode == 0:
    print("Comando executado corretamente: ")
    print(rede.stdout)
else:
    print("Erro ao executar o comando...")"""

#TRACERT
comando = subprocess.run(["tracert", "www.google.com.br"], capture_output=True, text=True)
if comando.returncode == 0:
    print("Comando executado: ")
    print(comando.stdout)
else:
    print("Erro ao executar o comando...")


