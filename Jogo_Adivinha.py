from random import randint
computador = randint (1, 100)

print(  "Bem vindo ao jogo adivinhe o número.\n"
        "Acabei de pensar em um número entre 1 e 100. "
        "Tente descobrir esse número.\n"
        "Digite sair para parar de jogar.\n",
)



acertou = False
palpites = 0
while not acertou:
        usuario = int(input("Qual número que eu pensei?"))
        palpites += 1

        if usuario == computador:
                 acertou = True
        else:
                 if usuario < computador:
                         print("Muito baixo! Eu pensei em um número maior.\n")
                 elif usuario > computador:
                         print ("Muito alto! Eu pensei em um número menor.\n")


print ("Acertou com {} tentativas. Muito bem!" .format(palpites))