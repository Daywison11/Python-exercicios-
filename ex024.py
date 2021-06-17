#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cd = input('Em que cidade voce nasceu?').upper().strip()
print(cd[:5]== 'SANTO')
