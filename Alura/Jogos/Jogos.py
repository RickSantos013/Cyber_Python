import Alura.Jogos.Forca as Forca
import Alura.Jogos.Adivinhacao as Adivinhacao

def escolhe_jogo():
  print("✯✯✯✯")
  print("JOGOS")
  print("✯✯✯✯")

  print("[1] Adivinhação [2] Forca")
  jogo = int(input("Escolha o jogo: "))

  if(jogo == 1):
      print("Jogando Adivinhação")
      Adivinhacao.jogar()
  elif(jogo == 2):
    print("Jogando Forca")
    Forca.jogar()

if(__name__ == "__main__"):
   escolhe_jogo()



