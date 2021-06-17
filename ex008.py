"""crie um programa que leia um valor em metros e transforme em centimetros e milimetros """

mtr = float(input('digite o valor em metros para ser convertido :'))
cet = (mtr * 100)
mlt = (mtr * 1000)
print('esse valor convertido em centimetros é {} e convertido em milimetros é {}'.format(cet,mlt))