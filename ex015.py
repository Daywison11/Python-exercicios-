#Escreva um programa que pergunte a quantidade de Km percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = int(input("por quantos dias o carro foi alugado?"))
km  = float(input('quantos km o carro percorreu?'))
s1  = (60*dia)
s2  = (km*0.15)
tt  = (s1+s2)
print('o valor total a ser pago pelo augeul do carro é de R${:.2f} '.format(tt))