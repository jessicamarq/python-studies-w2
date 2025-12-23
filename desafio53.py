frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
letras = ''.join(palavras)
invertido = letras[::-1]
if (invertido == letras):
  print('A frase É UM palídromo')
else:
  print('NÃO É um palídromo')