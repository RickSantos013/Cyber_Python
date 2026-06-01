from collections import Counter

#Criando arquivo de log
arquivo_log = "acessos.log"
#Criando lista para armazenar eventos suspeitos
tentativas_suspeitas = []

#Lendo arquivo
with open (arquivo_log, "r", encoding="utf-8") as f:
    for linha in f:
        #cada linha: data - ip - método/endpoint - código
        partes = linha.strip().split("-")
        if len(partes) != 4:
            continue #ignora linhas mal formatadas
        data, ip, recurso, codigo = partes
        codigo = int(codigo)
    #criterio de suspeita
    #1 falha de login 
    #2 acesso externo à area administrativa
    if codigo == 401 or "/admin" in recurso:
        tentativas_suspeitas.append(ip)

#Exibindo os resultados
contador_suspeitos = Counter(tentativas_suspeitas)
print(f"Resumo de IP's suspeitos: {contador_suspeitos}")
for ip, cont in contador_suspeitos.items():
    print(f"{ip} -> {cont} eventos suspeitos")

#Salvando relatório
with open ("relatorio_analise.txt", "w", encoding="utf-8") as f:
    for ip, cont in contador_suspeitos.items():
        f.white(f"{ip} -> {cont} eventos suspeitos\n")
