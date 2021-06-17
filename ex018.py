#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
import math
ag = float(input('digite o angulo que você deseja:'))
sn = math.sin(math.radians(ag))
cs = math.cos(math.radians(ag))
tg = math.tan(math.radians(ag))
print('O angulo de {} tem o seno de {:.2f}'.format(ag,sn))
print('O angulo de {} tem o coseno de {:.2f}'.format(ag,cs))
print('O angulo de {} tem o tangente de {:.2f}'.format(ag,tg))
