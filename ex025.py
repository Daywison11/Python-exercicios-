# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('qual e o seu nome completo?')).upper().strip()
print ('Seu nome tem silva? {}'.format('SILVA' in nome))