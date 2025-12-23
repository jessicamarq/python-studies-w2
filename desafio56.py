#refazer esse exercício
soma = 0
cont_f = 0
mais_velho = ''
maior_idade = 0
for i in range(1,5):
  nome = str(input(f'Digite o nome da {i}a pessoa: '))
  idade = int(input(f'Digite o idade da {i}a pessoa: '))
  sexo = str(input(f'Digite o sexo da {i}a pessoa: ')).lower()
  soma = soma + idade
  if (idade<20) and (sexo == 'f'):
    cont_f+=1
  if i == 1: # (Opcional: lógica pra garantir o primeiro)
    maior_idade = idade
    mais_velho = nome
  if idade > maior_idade:
    maior_idade = idade
    mais_velho = nome   
print(f'A média das idades do grupo é {soma/4} anos')
print(f'{cont_f} pessoas são mulheres que estão abaixo de 20 anos')
print(f'O homem mais velho tem {maior_idade} anos e se chama {mais_velho}')