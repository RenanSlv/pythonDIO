#Deposito
#Saque
#Estrato

# Todos depositos devem ser armazenados em uma variavel e exibidos 
# na operação de extrato
# 3 saques diários. R$500 max

menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair 

    => """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        print('====Depósito====')
        deposito = float(input('Digite o valor do depósito: '))

        if deposito <= 0:
            print('Valor de depósito inválido tente novamente.')
            continue

        saldo += deposito
        extrato += f'Deposito : R${deposito:.2f}\n'

    elif opcao == 's':
        print('====Saque====')
        saque = float(input('Digite o valor do saque (max R$500.00 por saque):'))
        
        if numero_saques == LIMITE_SAQUES:
            print('Saque não realizado. Você já atingiu o valor máximo de saques.')
            continue

        elif saque > saldo:
            print('Saque não realizado. Saldo insuficiente.')
            continue

        elif saque > 500 :
            print('Saque não realizado. O valor excede o valor máximo de saque.')
            continue
        
        elif saque <= 0:
            print('Saque não realizado. Valor de saque inválido.')
            continue

        else:
            saldo -= saque
            extrato += f'Saque : R${saque:.2f}\n'
            numero_saques += 1
        

    elif opcao == 'e':
        print('\n===============Extrato===============\n')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('=====================================')
    
    elif opcao == 'q':
        print('====Sair====')
        break

    else:
        print('========')
        print('Operação inválida, por favor selecione novamente a operação desejada.\n')

