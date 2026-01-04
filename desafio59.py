# crie um programa que leia dois valores e mostre um menu na tela: [1]somar, [2] multiplicar, [3]maior, [4]novos números, [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso. 

num1 = int(input('Digite o 1o número: '))
num2 = int(input('Digite o 2o número: '))
opcao = 0
while opcao != 5:
  print('-'*20)
  print('Selecione uma opção: ')
  print('-'*20)
  print('[1]SOMAR')
  print('[2]MULTIPLICAR')
  print('[3]MAIOR')
  print('[4]NOVOS NÚMEROS')
  print('[5]SAIR DO PROGRAMA')
  print('-'*20)
  opcao = int(input('>>>Selecione sua opção: '))
  if opcao == 1:
    soma = num1+num2
    print(f'A soma dos números é {soma}')
  elif opcao == 2:
    mult = num1*num2
    print(f'A multiplicação dos números é {mult}')
  elif opcao == 3:
    if num1>num2:
      print(f'O maior número é {num1}')
    else:
      print(f'O maior número é {num2}')
  elif opcao == 4:
    print('Informe os números novamente...')
    num1 = int(input('Digite o 1o número: '))
    num2 = int(input('Digite o 2o número: '))
  elif opcao == 5:
    print('Saindo do programa...')
  else:
    print('Opção inválida tente novamente.')