#Faça um programa que jogue par ou ímpar com um computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou ao final do jogo.

from random import randint
cont = 0
while True:
  num = int(input('DIGITE O NÚMERO PARA JOGAR: '))
  random = randint(1,5)