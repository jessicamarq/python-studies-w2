h = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
imc = p/(h*h)
if (imc<18.5):
  print(f'Seu IMC={imc:.2f} e você está abaixo do peso.')
elif(imc>=18.5) and (imc<25):
  print(f'Seu IMC={imc:.2f} e você está no peso ideal.')
elif(imc>=25) and (imc<30):
  print(f'Seu IMC={imc:.2f} e você está com sobrepeso.')
elif(imc>=30) and (imc<40):
  print(f'Seu IMC={imc:.2f} e você está com obesidade.')
else:
  print(f'Seu IMC={imc:.2f} e você está com obesidade mórbida.')
