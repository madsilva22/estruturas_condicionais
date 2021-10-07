"""
Faça um programa que receba 3 numeros e mostre o maior

"""
n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

if n1>n2 and n1>n3:
    print(f'{n1} é maior')
elif n2>n1 and n2>n3:
    print(f'{n2} é maior')
else:
    print(f'{n3} é maior')