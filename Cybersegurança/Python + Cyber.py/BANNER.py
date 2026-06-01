import socket

def banner_grabber(ip, port):
    try:
        #Criando um socket
        s = socket.socket
        s.settimeout(2)   #tempo máximo para a resposta(seg)
        #conectando IP e a porta
        s.connect((ip, porta))
        #Recebendo dados (banner)
        banner = s.recv(1024)
        #Exibindo banner decodificado
        print(f"[+] Banner de {ip}:{port} => {banner.decode().strip()}")
    except Exception as e:
        print(f"[-] Não foi possível coletar banner de {ip}:{port} => {e}")
    finally:
        s.close()

#Exemplo de uso
alvo_ip = "scanme.nmap.org"
alvo_portas = [21,22,80]
for porta in alvo_portas:
    banner_grabber(alvo_ip, porta)