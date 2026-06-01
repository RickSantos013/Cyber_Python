#Biblioteca Time
#Controle de tempos, cronômetros e medições de perfomance

import time

def contagem_regressiva(segundos):
    while(segundos > 0):
        print(f"Tempo restante: {segundos} segundos")
        time.sleep(1)   #pausa de 1s
        segundos -= 1
    print("Tempo esgotado")

#Iniciar contagem regressiva
contagem_regressiva(10)
