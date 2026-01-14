#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
#A: Qual é o total gasto na compra
#B: Quantos produtos custam mais do que R$1000
#C: Qual é o nome do produto mais barato

soma = 0
cont_mil = 0
menor = 0
barato = ' '
cont_volta = 0
while True:
  nome = str(input('Digite o nome do produto: '))
  valor = float(input('Digite o valor do produto: '))
  cont_volta += 1
  soma += valor

  if valor > 1000:
    cont_mil += 1
  if cont_volta == 1 or valor < menor:
    menor = valor
    barato = nome
  
  seguir = ' '
  while seguir not in 'SN':
    seguir = str(input('Você deseja continuar? [S/N]: ')).upper().strip()[0]
  if seguir == 'N':
    break
print(f'O total gasto na compra foi de R${soma:.2f} reais')
print(f'{cont_mil} produtos custam mais de R$1.000,00')
print(f'O produto de menor valor é {barato}')
