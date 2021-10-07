"""
O preco, a consumidor, de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor
e com impostos, ambos aplicados ao custo de fábrica. As porcetagens encontram-se na tablea a seguir.
Faça um programa que receba o custo da fabrcs de um carro e mostre o preço ao consumidor.

CUSTO DE FABRICA                % DO DISTRIBUIDOR               % DOD IMPOSTOS
até R$12.000,00                           5                         isento
R$12.000,00 - R$25.000,00                 10                          15
acima de R$25.000,00                      15                          20

"""

print('Fabrica de Carros Marcão')

vfab = float(input('Digite o Valor do Carro:'))

if 0 < vfab <= 12000:

    vdist = vfab * 0.05
    vtotal = vfab + vdist

    print(f'Custo de Fábrica: R${vfab} \n'
          f'Custo do Distribuidor: R${vdist} \n'
          f'Carro Isento de Imposto \n'
          f'Valor de Venda ao Consumidor: R${vtotal}')

elif 12000 < vfab <= 25000:

    vdist = vfab * 0.10
    vimp = vfab * 0.15
    vtotal = vfab + vdist + vimp
    print(f'Custo de Fábrica: R${vfab} \n'
          f'Custo do Distribuidor: R${vdist} \n'
          f'Valor do Imposto: R${vimp} \n'
          f'Valor de Venda ao Consumidor: {vtotal}')
elif vfab > 25000:

    vdist = vfab * 0.15
    vimp = vfab * 0.20
    vtotal = vfab + vdist + vimp
    print(f'Custo de Fábrica: R${vfab} \n'
          f'Custo do Distribuidor: R${vdist} \n'
          f'Valor do Imposto: R${vimp} \n'
          f'Valor de Venda ao Consumidor: {vtotal}')
else:
    print('Valor de Incorreto')
