num = int(input('Digite um número para converter: '))
print('1-Conversão para binário')
print('2-Conversão para octal')
print('3-Conversão para hexadecimal')
escolha = int(input('Agora, digite o número correspondente para conversão: '))
if (escolha == 1):
  print(f'O número digitado em binário é {bin(num)}')
elif (escolha == 2):
  print(f'O número digitado em octal é {oct(num)}')
else:
  print(f'O número digitador em hexadecimal é {hex(num)}')