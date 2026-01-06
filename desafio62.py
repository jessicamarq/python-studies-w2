#Melhore o desafio 61, perguntando para o usuário se ele quer que mostre mais alguns termos. O programa encerra quando ele diz que quer que mostrar 0 termos

a1 = int(input('Digite o 1o termo: '))
r = int(input('Digite a razão da PA: '))
termo = a1
total = 0
mais = 10
cont = 1

while mais != 0:
  total = total + mais
  while cont <= total:
    print(f'{termo} -> ', end=' ')
    termo += r
    cont += 1
  print('PAUSA')
  mais = int(input('Quantos termos você gostaria de mostrar a mais? '))

print('Progressão finalizada...')