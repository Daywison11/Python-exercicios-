#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
nm = int(input('digite um numero qualquer en 0 e 9999:'))
n = str(nm)
print('analizando o nunero {}'.format(nm))
print('unidade {}'.format(n[3]))
print('dezenas {}'.format(n[2]))
print('centena {}'.format(n[1]))
print('milhares {}'.format(n[0]))


