valorCasa = float(input('Digite o valor da casa: '))
valorSalario = float(input('Digite o valor do salário do comprador: '))
tempo = float(input('Digite em quantos anos pretende pagar: '))
prestacao = valorCasa/(tempo*12)
if (prestacao <= valorSalario*0.30):
  print(f'O valor da prestação é R${prestacao:.2f} e seu empréstimo foi aprovado!')
else:
  print('O valor da prestação excede %d%% do seu salário.' % 30)
  print('Empréstimo negado!')