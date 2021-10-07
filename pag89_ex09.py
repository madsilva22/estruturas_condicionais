"""
Um banco concedera um credito especial aos seus clientes, de acordo com o saldo médio no ultimo ano.
Faça um programa que receba o saldo medio de um clinete e calcule o valor medio do credito, de acordo
com a tabela a seguir. Mostre o saldo medio e o valor do credito.

            SALDO MEDIO                             PERCENTUAL
            > R$400,00                              30% DO SALDO MEDIO
            R$400,00 - R$300,00                     25% DO SALDO MEDIO
            R$300,00 - R$200,00                     20% DO SALDO MEDIO
            ATE R$200,00                            10% DO SALDO MEDIO

"""
nome = input('Digite Seu Nome: ')
saldo = float(input('Digite Seu Saldo Médio do Último Ano:'))

if saldo <= 200:
    credito = saldo * 1.10
    print(f'Caro {nome}, \n'
          f'Seu Saldo Médio é de R${saldo} \n'
          f'Valor de Crédito concedido é de 10%, no valor total de: R${credito}')
elif 200 < saldo <= 300:
    credito = saldo * 1.20
    print(f'Caro {nome}, \n'
          f'Seu Saldo Médio é de R${saldo} \n'
          f'Valor de Crédito concedido  é de 20%, no valor total de R${credito}')
elif 300 < saldo <= 400:
    credito = saldo * 1.25
    print(f'Caro {nome}, \n'
          f'Seu Saldo Médio é de R${saldo} \n'
          f'Valor de Crédito concedido é de 25%, no valor total de R${credito}')
else:
    credito = saldo * 1.30
    print(f'Caro {nome}, \n'
          f'Seu Saldo Médio é de R${saldo} \n'
          f'Valor de Crédito concedido é de 30%, no valor total de R${credito}')