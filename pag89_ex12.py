"""
Faça um programa que receba o salário brut de um funcionario e , usando a tabela a seguir, calcule e
mostre o valor a receber. Sabe-se qe este é composto pelo salário do funcionário acrescido de gratificação
e descontado o imposto de 7% sobre o salário sem gratificação.

                                    TABELA DE GRATIFIAÇÕES
                            SALÁRIO                        GRATIFICAÇÃO
                        até R$350,00                       R$100,00
                        R$350 - R$600                      R$75,00
                        R$600 - R$900                      R$50,00
                        acima de R$900                     R$35,00

"""
sal = float(input('Digite o salario do Funcionário: '))

if 0 < sal <= 350:
    saliq = sal * 0.07
    salt = sal + saliq + 100.0
    print(f'Salário Bruto: R${sal} \n'
          f'Valor do Imposto: R${saliq} \n'
          f'Gratificação: R$100,00 \n'
          f'Valor a Receber: R${salt}')

elif 350 < sal <= 600:
    saliq = sal * 0.07
    salt = sal + saliq + 75.0
    print(f'Salário Bruto: R${sal} \n'
          f'Valor do Imposto: R${saliq} \n'
          f'Gratificação: R$75,00 \n'
          f'Valor a Receber: R${salt}')

elif 600 < sal <= 900:
    saliq = sal * 0.07
    salt = sal + saliq + 50.0
    print(f'Salário Bruto: R${sal} \n'
          f'Valor do Imposto: R${saliq} \n'
          f'Gratificação: R$50,00 \n'
          f'Valor a Receber: R${salt}')

elif sal > 900:
    saliq = sal * 0.07
    salt = sal + saliq + 35.0
    print(f'Salário Bruto: R${sal} \n'
      f'Valor do Imposto: R${saliq} \n'
      f'Gratificação: R$35,00 \n'
      f'Valor a Receber: R${salt}')

else:
    print('Salario é Negativo!')