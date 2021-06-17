#: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na
# tela se o usuário venceu ou perdeu.
import random
import time
print('\033[;36m=-=\033[m'*20)
print('\033[0;33mvou pensar em um numero de entre 0 e 5. tente adivinhar \033[m')
print('\033[;36m=-=\033[m'*20)
time.sleep(1)
numero = int(input('\033[97mEM QUAL NUMERO EU PENSEI ?\33[m'))
computador = random.randint(0,5)
print('\033[31mPROCESSANDO\033[m')
time.sleep(0.5)
print('\033[31m.')
time.sleep(0.5)
print('.')
time.sleep(0.5)
print('.\033[m')
time.sleep(0.5)
if numero == computador:
    print('\033[36mPARABENS VOCÊ ACERTOU!!!!\033[m')
else:
    print('\033[33mQUE PENA VOCÊ EEROU!')
    print('O NUMERO QUR EU PENSEI FOI O NUMERO\033[M \033[36m{}\033[m'.format(computador))