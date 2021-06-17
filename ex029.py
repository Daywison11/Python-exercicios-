#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00
# por cada Km acima do limite.
vel = float(input('\033[97mQual a velocidade do carro?\033[m'))
mut = (vel - 80) * 7
if vel >= 35 and vel<=80:
    print('\033[32mTenha um bom dia! Dirija com cuidado!!!\033[m')
elif vel<=35:
    print('\033[33mALERTA!!! Você esta muito abaixo da velocidade ade na media!!!\033[m')
else:
    print('\033[31mMULTADO!!! Você excedeu o limite de velocidade que e pérmitido de 80km/h')
    print('você deverar pagar uma multa de \033[m\033[33mR${:.2f}\033[m'.format(mut))
    print('\033[97mDirija com cuidado! Tenha um bom dia!\033[m')
