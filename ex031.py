# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = int(input('Digite a distancia da viagem em km:'))
vic = (km * 0.50)
vil = (km * 0.45)
if km <= 200:
    print('Você esta prestes a iniciar uma viagem de {}km.'.format(km))
    print('E o preço da sua passagem vai ser de R${:.2f}'.format(vic))
else:
    print('Você esta prestes a iniciar uma viagem de {}km'.format(km))
    print('E o preço da sua viagem vai ser de R${:.2f}'.format(vil))
