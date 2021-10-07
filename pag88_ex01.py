"""
Faça um programa que receba 4 notas de um aluno, calcule e mostre a média aritmética
das notas e a mensagem de aprovado ou reprovado, considerando para aprovaçao a média é 7
"""

aluno = input('Digite o Nome do Aluno:')
n1 = int(input('Digite a Primeira Nota:'))
n2 = int(input('Digite a Segunda Nota:'))
n3 = int(input('Digite a Terceira Nota:'))
n4 = int(input('Digite a Quarta Nota:'))

media = (n1+n2+n3+n4)/4

if media>=7:
    print(f'Aluno {aluno} está aprovado com média {media}!!!')
else:
    print(f'Aluno {aluno} está reprovado com media {media}')

