#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
v1 = int(input('digite o primeiro valor:'))
v2 = int(input('digite o segundo valor:'))
v3 = int(input('digite o terceiro valor:'))
if v1 > v2 and v1 > v3:
    print('O maior valor digitado foi {}'.format(v1))
elif v1 < v2 and v1 < v3 :
    print('O menor valor digitado foi {}'.format(v1))
if v2 > v1 and v2 > v3 :
    print('O maior valor digitado foi {}'.format(v2))
elif v2 < v1 and v2 < v3 :
    print('O menor valor digitado foi o {}'.format(v2))
if v3 > v1 and v3 > v2 :
    print('O maior valor digitado foi {}'.format(v3))
elif v3 < v1 and v3 <v2:
    print('o menor valor digitado foi {}'.format(v3))
