# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Digite o ano que deseja analizar?\n'
                'Ou coloque 0 para analizar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é um ano BISSEXTO.'.format(ano))
else:
    print('O ano {} não e um ano BISSEXTO.'.format(ano))