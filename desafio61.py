#Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input('Digite o 1o termo: '))
r = int(input('Digite a razão da PA: '))
termo = a1
cont = 1
while cont <= 10:
  print(f'{termo} -> ', end=' ')
  termo += r
  cont += 1
print('FIM')