#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.
slr = float(input('Qual é o valor do salario do funcionario:'))
c1 = (slr * 10) /100
c2 = (slr * 15)/100
if slr <=1250.00:
    print('quem ganhava R${:.2f} passa a ganhar R${:.2f} '.format(slr,slr+c2))
elif slr >1250.00:
    print('quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(slr,slr+c1))
