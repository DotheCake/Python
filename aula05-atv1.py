from os import system
system('cls')

def Soma(x, y):
    print('A soma dos numeros é: {}' .format(float(x) + float(y)))

def Subtrair(x, y):
    print('A soma dos numeros é: {}' .format(float(x) - float(y)))

def Multiplicacao(x, y):
    print('A soma dos numeros é: {}' .format(float(x) * float(y)))

def Divisao(x, y):
    try:
        print('A soma dos numeros é: {}' .format(float(x) / float(y)))
    except ZeroDivisionError as error:
        print(error)

op = 's'

while op == 's':
    n1 = input('Digite o primeiro numero: ')
    n2 = input('Digite o segundo o numero: ')

    print('1. Soma')
    print('2. Subtrair')
    print('3. Multiplicação')
    print('4. Divisão')

    opcao = int(input('Opção: '))
    if opcao == 1:
        Soma(n1, n2)
    if opcao == 2:
        Subtrair(n1, n2)
    if opcao == 3:
        Multiplicacao(n1, n2)
    if opcao == 4:
        Divisao(n1, n2)
    op = input('Deseja fazer outra conta? Se sim (s) se não (n)')