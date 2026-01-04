#Faça um programa que leia um número qualquer e mostre o seu fatorial. 
from math import factorial
num = int(input('Digite um número: '))
f = factorial(num)
print(f'O fatorial de {num}! é {f}')