from abc import ABC, abstractmethod, abstractproperty

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero_conta, cliente):
        self._saldo = 0
        self._agencia = '0001'
        self._numero_conta = numero_conta #int
        self._cliente = cliente #Cliente
        self._historico = Historico() 
    

    @classmethod
    def nova_conta(cls, cliente, numero_conta):
        return cls(numero_conta, cliente) #Conta

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero_conta(self):
        return self._numero_conta
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        
        if float(valor) > float(saldo):
            print('Não foi possível realizar o saque. Saldo insuficiente.')
            return False #bool

        elif float(valor) <= 0:
            print('Não foi possível realizar o saque. Valor inválido.')
            return False #bool
        
        else:
            self._saldo -= valor
            print('\n Saque realizado com sucesso. \n')
            return True

    def depositar(self, valor):
        if valor <= 0:
            print('Não foi possível realizar o depósito. Valor inválido.')
            return False

        self._saldo += valor
        print('\n Depósito realizado com sucesso. \n')
        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente):
        super().__init__(numero_conta, cliente)
        self.limite = 500
        self.limite_saques = 3

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.
                             transacoes if transacao['tipo'] == Saque.__name__])
    
        if valor > self.limite:
            print('Não foi possível realizar o saque. Excedeu o limite de saque.')
            return False  
        
        elif numero_saques >= self.limite_saques:
            print('Não foi possível realizar o saque. Excedeu o limite de saques diários.')
            return False  
        
        else:
            return super().sacar(valor)

    def __str__(self):
        return f'''
            Agência: {self.agencia}
            C/C:     {self.numero_conta}
            Titular: {self.cliente.nome}'''
    
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractproperty
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
 

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            'tipo': transacao.__class__.__name__, 'valor': transacao.valor
        })

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

def verifica_cliente(clientes, cpf):
    for cliente in clientes:
        if cliente.cpf == cpf :
            return cliente
    return False

def verifica_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    if len(cliente.contas) == 1:
        return cliente.contas[0]
    else:
        for conta in cliente.contas:
            print(conta)
        num_conta = int(input('Digite o numero da conta: '))

        #index = cliente.contas.numero_conta.index(num_conta)
        
        for conta in cliente.contas:
            if conta.numero_conta == num_conta:
                print(conta.numero_conta)
                return conta
        else:
            print('ERRO!')
            return
                

def criar_cliente(clientes):
    print('====Criando Novo Usuário====')
    cpf = input ('Informe o CPF(apenas numeros): ')
    cliente = verifica_cliente(clientes, cpf)

    if cliente:
        print('\n Não foi possível criar uma conta. CPF não cadastrado.\n')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = '21'
    endereco = 'aaa'

    cliente = PessoaFisica(endereco, cpf, nome, data_nascimento)

    clientes.append(cliente)

    print('\n Cliente criado com sucesso. \n')

def criar_conta(clientes, contas, numero_conta):
    print('====Criando Conta====')
    cpf = input ('Informe o CPF(apenas numeros): ')
    cliente = verifica_cliente(clientes, cpf)

    if (not cliente):
        print('Não foi possível criar a conta. Não exite cliente com esse CPF.')
        return

    conta = ContaCorrente(numero_conta, cliente)
    cliente.contas.append(conta)
    contas.append(conta)

    print('SUCESSO')

def depositar(clientes):
    print('====Depósito====')
    cpf = input ('Informe o CPF(apenas numeros): ')
    cliente = verifica_cliente(clientes, cpf)

    if (not cliente):
        print('Não foi possível fazer o depósito. Cliente não encontrado.')
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = verifica_conta_cliente(cliente)
    if (not conta):
        return
    
    cliente.realizar_transacao(conta,transacao)

def sacar(clientes):
    print('====Saque====')
    cpf = input ('Informe o CPF(apenas numeros): ')
    cliente = verifica_cliente(clientes, cpf)

    if (not cliente):
        print('Não foi possível fazer o saque. Cliente não encontrado.')
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = verifica_conta_cliente(cliente)
    if (not conta):
        return
    
    cliente.realizar_transacao(conta,transacao)

def exibir_extrato(clientes):
    print('====Extrato====')
    cpf = input ('Informe o CPF(apenas numeros): ')
    cliente = verifica_cliente(clientes, cpf)

    if (not cliente):
        print('Cliente não encontrado.')
    
    conta = verifica_conta_cliente(cliente)
    if (not conta):
        print('Cliente não possui conta.')
        return
    
    transacoes = conta.historico.transacoes

    extrato = ''
    if (not transacoes):
        extrato = 'Conta não possui movimentações.'

    else:
        for transacao in transacoes:
            extrato += f'\n{transacao['tipo']}: R$ {transacao['valor']:.2f}'
    
    print(extrato)
    print(f'\n--------\nSaldo: R$ {conta.saldo:.2f}')

def listar_contas(clientes):
    cpf = input('Informe o cpf do clinte(apenas numero): ')
    cliente = verifica_cliente(clientes, cpf)

    for conta in cliente.contas:
        print(conta)
        

#MAIN
contas = []
clientes = []

while True:
    opcao = menu()

    if opcao == 'd':
        depositar(clientes)

    elif opcao == 's':
        sacar(clientes)   

    elif opcao == 'e':
        exibir_extrato(clientes)

    elif opcao == 'nu':
        criar_cliente(clientes)

    elif opcao == 'lc':
        listar_contas(clientes)
    
    elif opcao == 'nc':
        numero_conta = len(contas) + 1
        criar_conta(clientes, contas, numero_conta)

    elif opcao == 'q':
        print('====Sair====')
        break

    else:
        print('========')
        print('Operação inválida, por favor selecione novamente a operação desejada.\n')


