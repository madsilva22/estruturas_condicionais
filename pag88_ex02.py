"""
Faça um programa que receba duas notas, calcule e mostre a média aritmética e a mensagem que se
encontra na tabela a seguir:
    Média Aritmética            MENSAGEM
       0 - 4                    Reprovado
       4 - 7                    Exame
       7 - 10                   Aprovado
"""
aluno = input('Digite o Nome do Aluno: ')

n1 = int(input('Nota 1 :'))
n2 = int(input('Nota 2 :'))

media = (n1+n2)/2

if media > 0 and media <= 4:
    print(f'{aluno} foi Reprovado com média {media}')
elif media > 4 and media <=7:
    print(f'{aluno} está de Exame com média {media}')
else:
    print(f'{aluno} foi Aprovado com média {media}')