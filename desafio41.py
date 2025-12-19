from datetime import date
data_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = data_atual-ano_nascimento
if (idade<=9):
  print('Atleta em categoria MIRIM')
elif(idade>9) and (idade<=14):
  print('Categoria INFANTIL')
elif(idade>14) and (idade<=19):
  print('Categoria JÚNIOR')
elif(idade == 20):
  print('Categoria SÊNIOR')
else:
  print('Categoria MASTER')