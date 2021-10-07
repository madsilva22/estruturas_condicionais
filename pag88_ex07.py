"""
Uma empresa decide dar um aumento de 30% ao funcionarios com salarios inferiores a R$500,00. Faça um
programa que receba o salrio do funcionario e emostre o valor do salario reajustado ou uma mensagem,
caso ele não tenha direito ao aumento.

"""

salario = float(input('Digite o Salario atual: '))

if salario > 0 and salario <= 500.0:
    salario1 = salario * 1.3
    print(f'Seu salario de {salario} foi reaustado e foi para {salario1}')
else:
    print('Voçê não tem Direito ao Aumento')