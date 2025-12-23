num = int(input('Digite o número para saber se é primo: '))
divisores = 0
for i in range(1, num+1):
  if(num % i == 0):
    divisores+=1

if (divisores==2):
  print(f'O número {num} é primo')
else:
  print(f'o número {num} não é primo pois consegue ser dividido {divisores} vezes')