# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
import math
num = int(input('\033[97mdigite um numero qualquer:'))
imp = num % 2
if imp == 0:
    print('O numero {} e um numero mpar'.format(num))
else:
    print('O numero {} e um numero impar\033[m'.format(num))