import socket

"""#definição dos protocolos usados na requisição
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#escolha do servidor (site) a receber a requisição
client.connect(("google.com", 80))
#requisitando conexão
client.send(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")
response = client.recv(4096)
print(response.decode())

#lista de portas para testar
portas_para_testar = [21,22,23,80,443]
#IP ou HOSTNAME do alvo
alvo = "google.com.br"
print(f"Testando conexões com o host: {alvo}")

#limite de tempo de espera para conexão
for porta in portas_para_testar:            
    client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) #(IPV4 ou IPV6 | AF_INET ou AF_INET6, protocolo TCP)
    client.settimeout(1)

    try:
        client.connect((alvo, porta))
        print(f"[+] porta {porta} aberta!")
    except:
        print(f"[-] porta {porta} fechada!") 
    finally:
        client.close()"""


alvo = "scanme.nmap.org"  #192.168.68.55
#faixa de portas a serem testadas
for porta in range(1,1025):
    client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client.settimeout(0.5)

    conexao = client.connect_ex((alvo, porta))

    if conexao == 0:
        print(f"[+] porta {porta} aberta!")
        client.close()

"""
alvo = "scanme.nmap.org" #input("Digite o IP/HOST que deseja scanear: ")
intervalo_portas = int(input("Informe o intervalo de portas: "))

for porta in range(1,intervalo_portas + 1):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    conexao = client.connect_ex((alvo, porta))
    if conexao == 0:
        print(f"[+] porta {porta} aberta!")    
        client.close()"""