#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome
# do escolhido.
import random
al1 = (input('digite o nome do primeiro aluno:'))
al2 = (input('digite o nome do segundo aluno:'))
al3 = (input('digite o nome do terceiro aluno:'))
al4 = (input('digit o nome do quarto aluno:'))
alunos = [al1,al2,al3,al4]
sorteado = random.choice(alunos)
print('o aluno sorteado foi {}'.format(sorteado))