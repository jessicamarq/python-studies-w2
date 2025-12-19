valor = float(input('Digite o valor do produto: '))
print('1-A VISTA DINHEIRO/CHEQUE com 10% de desconto')
print('2-A VISTA NO CARTÃO com 5% de desconto')
print('3-EM 2x NO CARTÃO - SEM desconto')
print('4-EM 3x ou mais no cartão com juros da maquineta')
entrada = int(input('Escolha o valor correspondente a forma de pagamento...'))
if (entrada==1):
  print(f'O valor final do produto foi R${valor-(valor*0.10):.2f}')
elif(entrada==2):
  print(f'O valor final do produto foi R${valor-(valor*0.05):.2f}')
elif(entrada==3):
  print(f'O valor final do produto foi R${valor:.2f} em 2x de {valor/2}')
else:
  print(f'O valor final do produto foi R${valor*1.20:.2f}')