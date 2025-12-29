#melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint
sorteio = randint(0,10)
print('Sou seu computador e estou pensando em um número de 0 a 10. ')
num = int(input('Tente adivinhar... Qual seu palpite? '))
cont = 1
while num != sorteio:
  if num < 0 or num > 10:
    print('Opção inválida!')
    num = int(input('Tente de novo com um número válido: '))
    continue
  cont+=1
  if num < sorteio:
    print('Você errou! Tente um número maior...')
  else:
    print('Você errou! Tente um número menor...')
  num = int(input('Mais uma vez: '))
print(f'Você acertou! Estava pensando no número {num} e você levou {cont} tentativas para acertar!')  