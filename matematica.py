i = True

def menu():
    print('------Bem vindo a calculadora------')
    print('Operadores matemáticos\n+\n-\n*\n/')

def programa():
    if operador == '+':
        soma = valor1 + valor2
        print(f'O resultado é {soma}!')

    if operador == '-':
        soma = valor1 - valor2
        print(f'O resultado é {soma}!')

    if operador == '*':
        soma = valor1 * valor2
        print(f'O resultado é {soma}!')

    if operador == '/':
        soma = valor1 / valor2
        print(f'O resultado é {soma}!')

while i == True:
    menu()
    try:
        operador = input('Digite o operador matemático: ')
        if operador in ['+', '-', '*', '/']:
            valor1 = int(input('Digite o primeiro valor: '))
            valor2 = int(input('Digite o segundo valor: '))
            programa()
            p = input('Deseja rodar o programa novamente? Y/N: ')
            p.lower()
            if p != 'y':
                i = False
        else:
            print('Digite um operador válido!')
            p = input('Deseja rodar o programa novamente? Y/N: ')
            p.lower()
            if p != 'y':
                i = False

    except ValueError:
        print('Digite um valor válido!')
        if i == True:
            p = input('Deseja rodar o programa novamente? Y/N: ')
            p.lower()
            if p != 'y':
                i = False