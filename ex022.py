# Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input('digite seu nome completo:')).strip()
print('analizando seu nome...')
print('seu nome com todas as letras maiusculas é {}'.format(nome.upper()))
print('seu nome com todas as letras minusculas é {}'.format(nome.lower()))
print('seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))