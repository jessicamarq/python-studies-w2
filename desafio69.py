#crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: 
#A:Quantas pessoas têm mais de 18 anos
#B:Quantos homens foram cadastrados
#C:Quantas mulheres tem menos de 20 anos

cont_maior = 0
cont_h = 0
cont_f = 0
while True:
  nome = str(input('Digite o nome da pessoa: '))
  sexo = ' '
  while sexo not in 'MF':
    sexo = str(input('Digite o sexo da pessoa.[M/F]: ')).upper().strip()[0]
  idade = int(input('Digite a idade da pessoa: '))

  if idade >= 18:
    cont_maior+=1
  if sexo == 'M':
    cont_h+=1
  if sexo == 'F':
    cont_f+=1

  seguir = ' '
  while seguir not in 'SN':
    seguir = str(input('Você deseja continuar? [S/N]: ')).upper().strip()[0]
  if seguir == 'N':
    break
print(f'Há um total de {cont_h} homens')
print(f'Há um total de {cont_f} mulheres')
print(f'{cont_maior} pessoas estão acima de 18 anos')