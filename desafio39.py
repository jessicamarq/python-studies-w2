from datetime import date
data_atual = date.today().year
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = data_atual-ano_nascimento
if (idade < 18):
  print(f'Você ainda não pode se alistar. Faltam {18-idade} anos.')
elif (idade == 18):
  print('Você está em tempo de se alistar.')
elif (idade >18):
  print(f'Você está com {idade} anos e passou do prazo de alistamento há {idade-18} anos.')
