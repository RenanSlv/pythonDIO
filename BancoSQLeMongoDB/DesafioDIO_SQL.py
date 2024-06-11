from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect, select, func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import BINARY
from sqlalchemy import DECIMAL


Base = declarative_base()

class User(Base):
    __tablename__ = "Cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    cpf = Column(String(9))
    endereco = Column (String(50))

    conta = relationship(
        "Conta"
    )

    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco} )"

class Conta(Base):
    __tablename__ = "Conta_"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    numero = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("Cliente.id"), nullable=False)
    saldo = Column(DECIMAL)

    cliente = relationship(
        "User"
    )

    def __repr__(self):
        return f"Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, numero={self.numero}, id_cliente={self.id_cliente}, saldo={self.saldo})"

print(User.__tablename__)
print(Conta.__tablename__)

# Conexão com o banco de dados
engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)
print("*" * 20)
print(inspetor_engine.has_table("Cliente"))
print(inspetor_engine.has_table("Conta_"))

# Populando a tabela
with Session(engine) as session:
    joao = User(
        nome = 'João',
        cpf = '123456789',
        endereco = 'Rua ABC numero 123, bairro XYZ, cidade OK'
    )

    marina = User(
        nome = "Marina",
        cpf = "987654321",
        endereco = "Rua CBA numero 31, bairro XYZ, cidade OK",
        conta = [Conta(tipo="ContaCorrente",
                       agencia="0001",
                       numero=222, 
                       saldo=1500.50)]
    )

    marcos = User(
        nome = "Marcos",
        cpf = "111222333",
        endereco = "Rua CBA numero 456, bairro XYZ, cidade OK",
        conta = [Conta(tipo="ContaPupança",
                       agencia="0001",
                       numero=333, 
                       saldo=1234.56)]
    )

    session.add_all([joao, marina, marcos])
    session.commit()

   
stmt = select(User).where(User.nome.in_(["João", "Marina", "Marcos"]))
print('\nRecuperando usuários a partir de condição de filtragem')
for user in session.scalars(stmt):
    print(user)

stmt_marina_conta = select(Conta).where(Conta.id_cliente.in_([2]))
print('\nRecuperando os dados da conta da Marina')
for conta in session.scalars(stmt_marina_conta):
    print(conta)


stmt_join = select(User.nome, Conta.numero).join_from(Conta, User)
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()

print("Pegando o nome da conta e o numero da conta")
for result in results:
    print(result)


"""
    CLIENTE
    id = integer
    nome = string
    cpf = string(9)
    endereco = string

    
    CONTA
    id = binary
    tipo = string
    agencia = string
    numero = integer
    id_cliente integer
    saldo = decimal
"""

