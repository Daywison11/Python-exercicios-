#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('digite seu nome completo:'))
nm = nome.split()
print('muito prazer em te conhecer {}'.format(nome))
print('seu primeiro nome é {}'.format(nm[0]))
print('seu ultimo some é {}'.format(nm[len(nm)-1]))