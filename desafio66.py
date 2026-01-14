soma = 0
cont = 0
while cont >= 0:
  print('Digite 999 caso queira parar')
  n = int(input('ou um número inteiro: '))
  print('-'*30)
  if n == 999:
    break
  soma += n
  cont+=1
print(f'Você digitou {cont} números e a soma entre eles foi de {soma}')
print('Finalizando programa...')

