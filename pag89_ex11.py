"""
Faça um programa que receba o salário atual de um funcionário e, usando a tabela a seguir, calcule e
mostre o valor do aumento e o novo salário.

                SALÁRIO                         % DE AUMENTO
                até R$300                           15
                R$300 - R$600                       10
                R$600 - R$900                       5
                acima de R$900                      0

"""

sal = float(input('Digite o Salário: '))

if sal <= 300:

    val = sal * 0.15
    nsal = sal + val
    print(f'Salário atual: R${sal} \n '
          f'Valor do Aumento: R${val} \n'
          f'Novo Salario: R${nsal}')

elif 300 < sal <= 600:

    val = sal * 0.10
    nsal = sal + val
    print(f'Salário atual: R${sal} \n '
          f'Valor do Aumento: R${val} \n'
          f'Novo Salario: R${nsal}')


elif 600 < sal <= 900:

    val = sal * 0.05
    nsal = sal + val
    print(f'Salário atual: R${sal} \n '
          f'Valor do Aumento: R${val} \n'
          f'Novo Salario: R${nsal}')

else:
    print('O Funcionario não tem direito a aumento')