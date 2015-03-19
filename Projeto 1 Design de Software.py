# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:07:35 2015

@author: andre_000
"""

import random
jogador = 0
com = 0
while com<3 and jogador<3:
    computador = ["pedra","papel", "tesoura", "spock","lagarto"]
    sorteio = random.choice(computador)
    jogador1 = input("Qual opção é a desejada: pedra, papel, tesoura, spock, ou lagarto? ")
    jogador1 = jogador1.lower()
    if sorteio == jogador1:
        print("Você jogou %s e o Computador %s, EMPATE"%(jogador1,sorteio))
        print("%s x %s"%(com,jogador))
    elif (sorteio == "pedra" and jogador1 == "papel"):
        print("Você jogou %s e o Computador %s, VOCÊ GANHOU!!"%(jogador1,sorteio))
        jogador = jogador+1
        com = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "pedra" and jogador1 == "tesoura"):
        print("Você jogou %s e o Computador %s, VOCÊ PERDEU!!"%(jogador1,sorteio))
        com =  com+1
        jogador = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "pedra" and jogador1 == "lagarto"):
        print("Você jogou %s e o Computador %s, VOCÊ PERDEU!!"%(jogador1,sorteio))
        com = com+1
        jogador = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "pedra" and jogador1 == "spock"):
        print("Você jogou %s e o Computador %s, VOCÊ GANHOU!!"%(jogador1,sorteio))
        jogador = jogador+1
        com = com+1
        print("%s x %s"%(com,jogador))
    elif (sorteio == "papel" and jogador1 == "pedra"):
        print("Você jogou %s e o Computador %s, VOCÊ PERDEU!!"%(jogador1,sorteio))
        com = com+1
        jogador = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "tesoura" and jogador1 == "papel"):
        print("Você jogou %s e o Computador %s, VOCÊ PERDEU!!"%(jogador1,sorteio))
        com = com+1
        jogador = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "papel" and jogador1 == "tesoura"):
        print("Você jogou %s e o Computador %s, VOCÊ GANHOU!!"%(jogador1,sorteio))
        jogador = jogador+1
        com = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "tesoura" and jogador1 == "lagarto"):
        print("Você jogou %s e o Computador %s, VOCÊ PERDEU!!"%(jogador1,sorteio))
        com = com+1
        jogador = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "lagarto" and jogador1 == "tesoura"):
        print("Você jogou %s e o Computador %s, VOCÊ GANHOU!!"%(jogador1,sorteio))
        jogador = jogador+1
        com = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "papel" and jogador1 == "spock"):
        print("Você jogou %s e o Computador %s, VOCÊ PERDEU!!"%(jogador1,sorteio))
        com = com+1
        jogador = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "spock" and jogador1 == "papel"):
        print("Você jogou %s e o Computador %s, VOCÊ GANHOU!!"%(jogador1,sorteio))
        jogador = jogador+1
        com = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "lagarto" and jogador1 == "spock"):
        print("Você jogou %s e o Computador %s, VOCÊ PERDEU!!"%(jogador1,sorteio))
        com = com+1
        jogador = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "spock" and jogador1 == "lagarto"):
        print("Você jogou %s e o Computador %s, VOCÊ GANHOU!!"%(jogador1,sorteio))
        jogador = jogador+1
        com = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "lagarto" and jogador1 == "papel"):
        print("Você jogou %s e o Computador %s, VOCÊ PERDEU!!"%(jogador1,sorteio))
        com = com+1
        jogador = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "papel" and jogador1 == "lagarto"):
        print("Você jogou %s e o Computador %s, VOCÊ GANHOU!!"%(jogador1,sorteio))
        jogador = jogador+1
        com = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "spock" and jogador1 == "tesoura"):
        print("Você jogou %s e o Computador %s, VOCÊ PERDEU!!"%(jogador1,sorteio))
        com = com+1
        jogador = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "tesoura" and jogador1 == "spock"):
        print("Você jogou %s e o Computador %s, VOCÊ GANHOU!!"%(jogador1,sorteio))
        jogador = jogador+1
        com = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "tesoura" and jogador1 == "pedra"):
        print("Você jogou %s e o Computador %s, VOCÊ GANHOU!!"%(jogador1,sorteio))
        jogador = jogador+1
        com = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "lagarto" and jogador1 == "pedra"):
        print("Você jogou %s e o Computador %s, VOCÊ GANHOU!!"%(jogador1,sorteio))
        jogador = jogador+1
        com = 0
        print("%s x %s"%(com,jogador))
    elif (sorteio == "spock" and jogador1 == "pedra"):
        print("Você jogou %s e o Computador %s, VOCÊ PERDEU!!"%(jogador1,sorteio))
        com = com+1
        jogador = 0
        print("%s x %s"%(com,jogador))
input("Você gostaria de jogar novamente? Se sim, recomeçe o jogo")


    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        