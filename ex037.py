#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
# Início
print('\033[7;4m=\033[m'*30)
print('\033[1;7m Conversor de bases numéricas \033[m')
print('\033[7;4m=\033[m'*30)
print('\nEste é um conversor de base decimal para binário, octal ou hexadecimal.'
      '\nPara usar, digite um número em decimal e em seguida, para qual base deseja converter.')
# Menu de Escolhas
numdecimal = int(input('Digite um número qualquer em decimal: '))
print('\n[ 1 ] para BINÁRIO'
      '\n[ 2 ] para OCTAL'
      '\n[ 3 ] para HEXADECIMAL')
escolha = int(input('\nQual será a sua escolha: '))
# Binário
if escolha == 1:
    numconvert = str(bin(numdecimal).replace('0b', ''))
    print('A conversão de decimal para binário dará o resultado de {}'.format(numconvert))
# Octal
elif escolha == 2:
    numconvert = str(oct(numdecimal).replace('0o', ''))
    print('\nA conversão de decimal para hexadecimal dará o resultado de {}'.format(numconvert))
# Hexadecimal
elif escolha == 3:
    numconvert = str(hex(numdecimal).replace('0x', ''))
    print('\n\nA conversão de decimal para hexadecimal dará o resultado de {}'.format(numconvert))