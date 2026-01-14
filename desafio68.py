#Faça um programa que jogue par ou ímpar com um computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou ao final do jogo.

from random import randint
cont = 0
while True:
  entrada = ' '
  while entrada not in 'PI':
    entrada = str(input('Você escolhe PAR ou ÍMPAR? [P/I]: ')).upper().strip()[0]
  
  num = int(input('Digite um número para jogar: '))
  computador = randint(0,10)
  resultado = num+computador
  
  tipo = 'Deu PAR' if resultado % 2 == 0 else 'Deu ÍMPAR'
  if tipo == 'Deu PAR':
    if entrada == 'P':
      print('Você venceeeu!')
      cont+=1
    else:
      print('Você perdeu!')
      break
  elif tipo == 'Deu ÍMPAR':
    if entrada == 'I':
      print('Você venceeeu!')
      cont+=1
    else:
      print('Você perdeu!')
      break     
  print('Vamos jogar novamente...')
print('GAME OVER!!')
print(f'Você venceu {cont} vezes')