#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

print('\033[34m-=-=-' * 20)
n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))
if n1 > n2:
    print('O PRIMEIRO valor é o maior!!!')
elif n1 == n2:
    print('Não existe valor maior os dois são iguais!')
else:
    print('O SEGUNDO valor é o maior!!!')
print('-=-=-' * 20)

