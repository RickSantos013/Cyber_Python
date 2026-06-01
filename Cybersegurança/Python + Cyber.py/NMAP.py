#Scanner simples
import nmap
import datetime
"""
scanner = nmap.PortScanner()                   #scaneando o IP
scanner.scan('192.168.0.1', '22-80')
print(scanner.all_hosts())                     #Listando todos os hosts
print(scanner['192.168.0.1'].state())          #Mostra se o host está UP ou DOWN
print(scanner['192.168.0.1'].all_protocols())  #Quais protocolos foram scaneados
print(scanner['192.168.0.1'].keys())           #Pegamos as portas abertas naquele IP

#Relatório Técnico
for host in scanner.all_hosts():
    print(f"Host: {host}")
    print(f"Estado: {scanner[host].state()}")

for proto in scanner[host].all_protocols():
    print(f"Protocolo: {proto}")

#Obter todas as portas scaneadas
ports = scanner[host][proto].keys()

#Ordena e percorre cada porta
for port in sorted(ports):
    estado = scanner[host][proto][port]['state']
    print(f"Porta: {port} | Estado: {estado}")"""

scanner = nmap.PortScanner()
#IP ou domínio que será analisado
alvo = "scanme.nmap.org"

#Intervalo de portas
portas = "20-100"

print(f"Iniciando varredura no alvo {alvo}...")
scanner.scan(alvo, portas, arguments="-T4") #arguments="-sV" mostra a versão "-T4"acelera o scan

#Criar nome do aquivo com data
data_atual = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
nome_arquivo = f"Relatório_{data_atual}.txt"

#Salvando os resultados no arquivo
with open(nome_arquivo,"w") as relatorio:
    for host in scanner.all_hosts():
        relatorio.write(f"HOST: {host} ({scanner[host].hostname()})\n")
        relatorio.write(f"STATUS: ({scanner[host].state()})\n")
        for protocolo in scanner[host].all_protocols():
            portas_abertas = scanner[host][protocolo].keys()
            for porta in portas_abertas:
                servico = scanner[host][protocolo][porta]['name']
                versao = scanner[host][protocolo][porta].get('version', "N/A")
                relatorio.write(f"Porta {porta}/{protocolo} -> {servico} {versao}\n")
print(f"Varredura concluída! Relatório salvo como {nome_arquivo}")

