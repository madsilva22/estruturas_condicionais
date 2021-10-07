"""
Faça um programa que receb 2 numeros e execute as operações listadas a seguir, de acordo
com a escolha do usuario

        ESCOLHA DO USUARIO              OPERAÇÃO
                1                   MÉDIA ENTRE OS NUMEROS DIGITADOS
                2                   DIFERENÇA DO MAIOR PELO MENOR
                3                   PRODUTO ENTRE OS NUMEROS DIGITADOS
                4                   DIVISÃO DO PRIMEIRO PELO SEGUNDO

"""

n1 = int(input('Digite o Numero 1: '))
n2 = int(input('Digite o Numero 2: '))

print('Menu de Opções')
print('Digite 1 - Média entre os Numeros Digitados \n'
      'Digite 2 - Diferença do Maior pelo Menor \n'
      'Digite 3 - Produto entre os Numeros Digitados \n'
      'Digite 4  - Divisão do Primeiro pelo Segundo Numero')

opt = int(input('Digite a Opção Desejada:'))

if opt == 1:
    media = (n1+n2)/2
    print(f'A média dos Numeros é: {media}')
elif opt == 2:
    diferenca = n1-n2
    print(f'A Diferença é de {diferenca}')
elif opt == 3:
    produto = n1*n2
    print(f'O Produto  é de {produto}')
elif opt == 4:
    divisao = n1/n2
    print(f'A Divisão é {divisao}')
else:
    print('Opção Errada!!!')