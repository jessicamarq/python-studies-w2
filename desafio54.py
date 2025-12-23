from datetime import date
ano_atual = date.today().year
cont_menor = 0
cont_maior = 0
for i in range (0,7):
  ano = int(input(f'Digite o ano de nascimento da {i+1}a pessoa:'))
  idade = (ano_atual-ano)
  if (idade<18):
    cont_menor+=1
  else:
    cont_maior+=1
print(f'Temos um total de {cont_menor} pessoas que não são maiores de idade e {cont_maior} acima de 18 anos')