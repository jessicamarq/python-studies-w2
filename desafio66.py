#Faça um programa que te mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
  num = int(input('Digite o número para saber a tabuada:'))
  print('Digite um número negativo para sair.')
  if num < 0:
    print('Encerrando programa...')
    break

  for i in range (1,11):
    print(f'{i} x {num} = {i*num}')
  print('Digite um número negativo para sair.')