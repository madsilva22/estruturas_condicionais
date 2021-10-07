salario = int(input('Digite o Salario: '))

if 0 < salario <= 300:
    nsalario = salario * 1.5
    print('Novo Salário = ', nsalario)
elif 300 < salario <= 500:
    nsalario = salario * 1.4
    print('Novo Salario = ', nsalario)
elif 500 < salario <= 700:
    nsalario = salario * 1.3
    print('Novo Salario = ', nsalario)
elif 700 < salario <= 800:
    nsalario = salario * 1.2
    print('Novo Salario = ', nsalario)
elif 800 < salario <= 1000:
    nsalario = salario * 1.1
    print('Novo Salario = ', nsalario)
else:
    nsalario = salario * 1.05
    print('Novo Salario = ', nsalario)


