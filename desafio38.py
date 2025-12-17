num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if (num1 > num2):
  print(f'O primeiro valor({num1}) é maior que o segundo({num2})')
elif (num1 < num2):
  print(f'O segundo valor({num2}) é maior que o primeiro({num1})')
else:
  print('Ambos os números são iguais')