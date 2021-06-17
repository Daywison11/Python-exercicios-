"""crie um programa que leia a autura e a largura de uma parede e calcule a sua area """
'e quantas latas de tintas necessaria para pintar sabeno que cada lata pinta are de 2m²'
a = float(input('qual a alturta da parede em metros:'))
l = float(input('qual a largura da parede em metros:'))
a = (l * a)
print('a area dessa parede e {}m²'.format(a))
t = (a / 2)
print('para pintar aparede voce ira precisar de {} litros de tintas'.format(t))
