preco = float(input('Digite o Preço do Produto: '))
categoria = int(input('Digite a Categoria do Produto (1, 2 ou 3):'))
situacao = input('Digite a Situação do Produto( R ou N )')

if 0 < preco <= 25:

    if categoria == 1:

        aumento = preco * 0.05
        imposto = preco * 0.08
        novoValor = preco + aumento
        print('Preço do Produto: ', preco)
        print('Categoria do Produto: Limpeza')
        print('Produto Não Necessita de Refrigeração')
        print('Valor do Aumento no Produto: ', aumento)
        print('Valor do Imposto do Produto: ', imposto)
        print('Novo Valor do Produto: ', novoValor)

    elif categoria == 2:
        if situacao == 'R':

            aumento = preco * 0.05
            imposto = preco * 0.05
            novoValor = preco + aumento
            print('Preço do Produto: ', preco)
            print('Categoria do Produto: Limpeza')
            print('Produto  Necessita de Refrigeração')
            print('Valor do Aumento no Produto: ', aumento)
            print('Valor do Imposto do Produto: ', imposto)
            print('Novo Valor do Produto: ', novoValor)
        else:

            aumento = preco * 0.05
            imposto = preco * 0.08
            novoValor = preco + aumento
            print('Preço do Produto: ', preco)
            print('Categoria do Produto: Limpeza')
            print('Produto Não Necessita de Refrigeração')
            print('Valor do Aumento no Produto: ', aumento)
            print('Valor do Imposto do Produto: ', imposto)
            print('Novo Valor do Produto: ', novoValor)

