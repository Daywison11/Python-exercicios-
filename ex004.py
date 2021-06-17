# faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e as informações possives sobre ela
a = input('digite algo:')
print('{} e numerico'.format(a))
print (a.isnumeric())
print('{} e alfabetico?'.format(a))
print(a.isalpha())
print('{} e alpha numerico'.format(a))
print(a.isalnum())
