"""
Faça um programa que receba 2 numeros e execute uma das operações listadas a seguir, de acordo
com a escolha do usuario. Se for digitada um opção invalida, mostre a mensagem de erro e termine
a execução do programa. As opções são:

1 - O primeiro numero elevado ao segundo numero
2 - Raiz quadrada de cada um dos numeros
3 - Raiz cubica de cada um dos numeros
"""

n1 = int(input('Digite o Numero 1:'))
n2 = int(input('Digite o Numero 2:'))

opt = int(input('Digite a Opção (1-3)'))

if opt == 1:
    potencia = n1 ** n2
    print(f'{n1} elevado a {n2} é: {potencia}')
elif opt == 2:
    raiz1 = n1 ** (1/2)
    raiz2 = n2 ** (1/2)
    print(f'Raiz Quadrada de {n1} é: {raiz1}')
    print(f'Raiz Quadrada de {n2} é: {raiz2}')
elif opt == 3:
    raiz1 = n1 ** (1/3)
    raiz2 = n2 ** (1/3)
    print(f'Raiz Cúbica de {n1} é: {raiz1}')
    print(f'Raiz Cúbica de {n2} é: {raiz2}')
else:
    print('Opção Errada!')