# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não
# pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
psal = (sal * 0.3) #30% do salário
prest = casa / (anos * 12) #prestação
print('Para pagar uma casa de R${} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prest))
if psal > prest:
    print('Sua situação se enquadra nas exigências \033[0;34m\nAPROVADO!')
elif psal <= prest:
    print('Sua situação não se enquadra nas exigências \033[0;31m\nNEGADO')
