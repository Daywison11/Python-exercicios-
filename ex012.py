"""faça um algoritimo que leia o preço de um produto e depois caucule o novo preço com 5% de desconto"""

s = float(input('qual  o preço atualmente :'))
s1 = (s * 5)
s2 = (s1 / 100)
s3 = (s - s2 )
print('o valor desse produto com desconto de 5% é {}'.format(s3))