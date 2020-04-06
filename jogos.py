import forca
import adivinhacao

print("*********************************")
print("-------  Escolha um jogo! -------")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo desja jogar?"))

if(jogo == 1):
    print("Forca iniciado!")
    forca.jogar()
elif(jogo == 2):
    print("Adivinhação iniciando!")
    adivinhacao.jogar()