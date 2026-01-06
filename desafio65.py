#crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário, se ele quer ou não continuar a digitar os valores. 

soma = 0
cont = 0
maior = None
menor = None
while True:
  n = int(input('Digite um número inteiro: '))
  soma += n
  cont+=1
  if maior is None or n > maior:
    maior = n
  if menor is None or n < menor:
    menor = n
  resposta = input('Deseja parar? [S/N] ').strip().upper()
  if resposta == 'S':
    break
if cont:
  media = soma/cont
  print(f'A média dos números digitados é {media}')
  print(f'O maior número é {maior} e o menor valor foi {menor}')
else:
  print('Nenhum número foi digitado...')