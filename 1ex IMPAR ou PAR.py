'''1. Faça um programa em Python que leia um número inteiro, em seguida, mostre na tela se o 
número digitado é par ou ímpar.'''

numero = int(input("Digite um numero : "))

if (numero % 2 ==0):
    print(f"O número digitado {numero}, é PAR!")
else:
   print(f"O número digitado {numero}, é IMPAR!")

