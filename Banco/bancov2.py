#Saque = keyword only -> saldo, valor, extrato, limite, numero_saques, limite_saques
#Deposito = positional only -> saldo, valor, extrato
#Extrado = positional (saldo) e keyword (extrato) 
#Duas funçoes nova: Criar usuário e criar conta corrente 
#Usuario: Nome, DtNascimento, CPF e Endereço. Endereço: logradouro, numero - bairro - cidade/sigla Estado.
#Não pode 2 usuários com o mesmo CPF
#Conta: Agencia, nConta, Usuario -> Numero da conta sequencial, agencia 0001


def menu():

    menu = input("""

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Criar nova conta
        [nu] Criar novo usuário
        [lc] Listar contas
        [q] Sair 

        => """)

    return menu

def depositar(saldo, valor_deposito, extrato, /):  
    if valor_deposito <= 0:
        print('Depósito não realizado. Valor do depósito invalido.')
        return saldo, extrato
    else:
        saldo += valor_deposito
        extrato += f'Deposito : R${valor_deposito:.2f}\n'
        return saldo, extrato

def saque(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    if numero_saques == limite_saques:
        print('Saque não realizado! Você já atingiu o valor máximo de saques por dia.')
        return saldo, extrato, numero_saques

    elif valor_saque > saldo:
        print('Saque não realizado! Saldo insuficiente.')
        return saldo, extrato, numero_saques

    elif valor_saque > limite :
        print('Saque não realizado! O valor excede o valor máximo de saque.')
        return saldo, extrato, numero_saques
        
    elif valor_saque <= 0:
        print('Saque não realizado! Valor de saque inválido.')
        return saldo, extrato, numero_saques

    else:
        saldo -= valor_saque
        extrato += f'Saque : R${valor_saque:.2f}\n'
        numero_saques += 1
        return saldo, extrato, numero_saques

def mostrar_extrato(saldo, /, *, extrato):
    print('\n===============Extrato===============\n')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R${saldo:.2f}')
    print('=====================================')

def verifica_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def criar_usuario(usuarios):
    print('====Criando Novo Usuário====')
    cpf = input ('Informe o CPF(apenas numeros): ')
    
    if verifica_usuario(cpf, usuarios) == None:
        usuario = {}
        usuario.update({'nome': input('Informe o nome: '),
                        'data_de_nascimento': input('Informe a data de nascimento (dd-mm-aaaa): '),
                        'cpf': cpf,
                        'endereco': {'logradoudo': input('Informe o logradouro: '),
                                    'numero': input('Informe o numero: '),
                                    'bairro': input('Informe o bairro: '),
                                    'cidade': input('Informe a cidade: '),
                                    'sigla_estado': input('Infome o estado (sigla): ')}})
        return usuario
    else:
        return

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    verificacao = verifica_usuario(cpf, usuarios)
    
    if  verificacao == None:
        print('Não foi possivel criar uma conta! Não exite usuário com esse CPF. ')
        return
    
    return {'agencia': agencia, 'conta': numero_conta + 1, 'usuario': verificacao['nome']}
    
def listar_contas(usuarios):
    print('====Listando Usuarios====')
    print(usuarios)
    


#MAIN
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'
usuarios = []
contas = []


while True:

    opcao = menu()

    if opcao == 'd':
        print('====Depósito====')
        valor_deposito = float(input('Digite o valor do depósito: '))

        saldo , extrato = depositar(saldo, valor_deposito, extrato)

    elif opcao == 's':
        print('====Saque====')
        valor_saque = float(input('Digite o valor do saque (max R$500.00 por saque):'))
        
        saldo, extrato, numero_saques = saque(saldo=saldo, valor_saque=valor_saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)     

    elif opcao == 'e':
        mostrar_extrato(saldo, extrato=extrato)

    elif opcao == 'nu':
        usuarios.append(criar_usuario(usuarios))

    elif opcao == 'lc':
        print(contas)
    
    elif opcao == 'nc':
        numero_conta = len(contas)
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
            print('Conta criada com sucesso!')


    elif opcao == 'q':
        print('====Sair====')
        break

    else:
        print('========')
        print('Operação inválida, por favor selecione novamente a operação desejada.\n')

