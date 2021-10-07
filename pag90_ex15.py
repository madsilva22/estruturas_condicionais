_tipoDeInvestimento = int(input('Digite o tipo de Investimento: 1 - Poupança; 2 - CDB: '))
_valorDoInvestimento = float(input('Digite o Valor do Inestimento:'))

if _tipoDeInvestimento == 1:

    _valorCorrigido = _valorDoInvestimento * 1.03

    print('Você Escolheu Poupança como Investimento')
    print('Valor Investido na Poupança =  ', _valorDoInvestimento)
    print('Valor Corrigido = ', _valorCorrigido)

else:

    _valorCorrigido = _valorDoInvestimento * 1.04

    print('Você Escolheu o CDB como Investimento')
    print('Valor Investido no CDB =  ', _valorDoInvestimento)
    print('Valor Corrigido = ', _valorCorrigido)

