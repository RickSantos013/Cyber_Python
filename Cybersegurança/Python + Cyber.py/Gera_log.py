import subprocess

ping = subprocess.run(["ping", "-n", "4", "google.com.br"], capture_output=True, text=True)
if ping.returncode == 0:
    print("**PING**")
    print("Conexão ativa!")
    print(ping.stdout)
else:
    print("Erro ao executar o ping...")

with open("log_ping.txt", "w") as log:    
    log.write(ping.stdout)


#netstat 
netstat = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
print("**NETSTAT**")
print(netstat.stdout)

with open("log_netstat.txt", "w", encoding="utf-8") as log:
    log.write(netstat.stdout)