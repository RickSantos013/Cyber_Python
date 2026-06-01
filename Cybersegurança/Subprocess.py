#Biblioteca subprocess
#Execução de comandos externos e automação de tarefas do SO

import subprocess

command = ["cmd", "/c" ,"dir"]
result = subprocess.run(command, text=True, capture_output=True)

#Exibe a saída
if result.returncode == 0:
    print("Saída do comando: ")
    print(result.stdout)
else:
    print("Erro ao executar o comando: ")
    print(result.stderr)

