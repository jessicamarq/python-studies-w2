#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F' caso esteja errado, peça a digitação novamente até ter um valor correto
sexo = str(input("Qual o sexo? [M/F]? ")).upper().strip()[0]
while (sexo != 'M') and (sexo != 'F'):
  sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')