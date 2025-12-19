nota1 = float(input('Digite a 1a nota: '))
nota2 = float(input('Digite a 2a nota: '))
media = (nota1+nota2)/2
if(media<5):
  print(f'Você tirou {media:.2f} e está REPROVADO(A)!')
elif(media>5) and (media<6.9):
  print(f'Você ficou com {media:.2f} e está de RECUPERAÇÃO')
else:
  print(f'Você foi APROVADO com média {media:.2f}')