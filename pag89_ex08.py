"""
Faça um programa para calcular e mostrar o salario reajustado de um funcionario. O percentual
de aumento encontra-se na tabela abaixo:

                SALÁRIO                                     PERCENTUAL DE AUMENTO
                até R$300,00                                            35%
                > R$300,00                                              15%
"""
sal1 = float((input('Digite o Salario: ')))

if sal1 <= 300.0:
    sal2 = sal1 * 1.35
    print(f'O salario de {sal1} foi ajustado em 35% e foi  para: {sal2}')
else:
    sal2 = sal1 * 1.15
    print(f'O salário de {sal1} foi ajustado em 15% e foi para: {sal2}')