#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa
import math
co = float(input('valor do cateto oposto:'))
ca = float(input('valor do cateto adjacente:'))
hi = math.hypot(co,ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))