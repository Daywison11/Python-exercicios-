# mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
al1 = (input('digite o nome do primeiro aluno:'))
al2 = (input('digite o nome do segundo aluno:'))
al3 = (input('digite o nome do terceiro aluno:'))
al4 = (input('digit o nome do quarto aluno:'))
alunos = [al1,al2,al3,al4]
random.shuffle(alunos)
print('a ordem sorteada sera')
print(alunos)

