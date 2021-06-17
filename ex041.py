#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de
# um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date
nasc = int(input('Digite o ano de nascimento do aluno: ').strip())
idade = date.today().year - nasc

#CATEGORIAS
mirim = range(0, 10)
infatil = range(10, 15)
junior = range(15, 20)
senior = 20

#CONDIÇÕES
if idade in mirim:
    print('MIRIM. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
elif idade in infatil:
    print('INFANTIL. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
elif idade in junior:
    print('JUNIOR. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
elif idade == senior:
    print('SENIOR. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))
else:
    print('MASTER. O aluno tem {} anos, então se encaixa nessa categoria.'.format(idade))

#FIM