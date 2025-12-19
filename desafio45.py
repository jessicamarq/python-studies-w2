from random import choice
jogo = [1,2,3]
sorteio = choice(jogo)
print('1-Pedra')
print('2-Papel')
print('3-Tesoura')
entrada = int(input('Digite o número correspondente: '))
if (sorteio==1) and (entrada==2):
  print('Você ganhou!')
elif(sorteio==1) and (entrada==3):
  print('Você perdeu!')
elif(sorteio==2) and (entrada==1):
  print('Você perdeu!')
elif(sorteio==2) and (entrada==3):
  print('Você ganhou!')
elif(sorteio==3) and (entrada==1):
  print('Você ganhou!')
elif(sorteio==3) and (entrada==2):
  print('Você perdeu!')
else:
  print('Deu empate!')