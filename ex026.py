#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase:')).upper().strip()
print('A letra A aprece {} veze na frase.'.format(frase.count('A')))
print('O primeiro A aprece na posição {}'.format(frase.find('A')+1))
print('O ultimo A aparece na posição {}'.format(frase.rfind('A')+1))
