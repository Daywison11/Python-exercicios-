#Crie um programa que leia um número Real qualquer
#pelo teclado e mostre na tela a sua porção Inteira
import math
n1 = float(input('digite um valor qualquer :'))
it = math.trunc(n1)
print('o valor digitado foi {} e a porção inteira desse numero é {}'.format(n1,it))