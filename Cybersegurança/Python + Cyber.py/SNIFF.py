"""
from scapy.all import sniff

#Função que vai ser chamada para cada pacote capturado
def pacote_recebido(pacote):
    print(pacote.summary())   #mostra um resumo do pacote capturado

#Inicia a captura de pacotes na interface padrão
print("Iniciando sniffing de pacotes...")

#sniff()  captura os pacotes. Aqui limitamos para 5 pacotes
sniff(count=5, prn=pacote_recebido) """

from scapy.all import IP, ICMP, send

#Criar pacote IP com origem e destino
pacote = IP(src = "10.0.0.123", dst = "8.8.8.8")
print("Enviando pacote ICMP com IP falso de origem...")
#Enviar pacote
send(pacote)
