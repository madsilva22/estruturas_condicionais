#pag89_ex13

v_prod = int(input('Digite o Valor do Produto: '))

if 0 < v_prod <= 50:
    nv_prod = v_prod * 1.05
    if 0 < nv_prod <= 80:
        print(f'Valor do Produto: R${v_prod} \n'
              f'Novo Valor do Produto: R${nv_prod} \n'
              f'O Produto está Barato!')


elif 50 < v_prod <= 100:
    nv_prod = v_prod * 1.10
    if 0 < nv_prod <= 80:
        print(f'Valor do Produto: R${v_prod} \n'
              f'Novo Valor do Produto: R${nv_prod} \n'
              f'O Produto está Barato!')
    if 80 < nv_prod <= 120:
        print(f'Valor do Produto: R${v_prod} \n'
              f'Novo Valor do Produto: R${nv_prod} \n'
              f'O Produto está Normal!')

elif v_prod > 100:
    nv_prod = v_prod * 1.15
    if 80 < nv_prod <= 120:
        print(f'Valor do Produto: R${v_prod} \n'
              f'Novo Valor do Produto: R${nv_prod} \n'
              f'O Produto está Normal!')
    elif 120 < nv_prod <= 200:
        print(f'Valor do Produto: R${v_prod} \n'
              f'Novo Valor do Produto: R${nv_prod} \n'
              f'O Produto está Caro!')
    else:
        print(f'Valor do Produto: R${v_prod} \n'
              f'Novo Valor do Produto: R${nv_prod} \n'
              f'O Produto está Muito Caro!')

else:
    print('Voce Digitou um Numero Negativo!')




