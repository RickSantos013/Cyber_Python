import subprocess


comando = subprocess.run(["ping", "-n", "4", "google.com.br"], capture_output=True, text=True)
if comando.returncode == 0:
    print("Saída: ")
    print(comando.stdout)
else:
    print("Erro ao executar o ping...")

#SYSTEM INFO
sistema = subprocess.run(["systeminfo"], capture_output=True, text=True)
print("INFORMAÇÕES DO SISTEMA:\n", sistema.stdout)

#HOSTNAME
host = subprocess.run(["hostname"], capture_output=True, text=True)
print("Nome: \n", host.stdout)

#TASKLIST
processos = subprocess.run(["tasklist"], capture_output=True, text=True)
print("Processos em execução: \n", processos.stdout)