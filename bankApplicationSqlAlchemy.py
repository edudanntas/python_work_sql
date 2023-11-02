from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nome = Column(String(40))
    cpf = Column(String(11))
    endereco = Column(String)

    addresses = relationship("Conta", back_populates="user")


class Conta(Base):
    __tablename__ = 'conta'

    id = Column(Integer, primary_key=True)
    tipo = Column(String, default='Conta Corrente')
    agencia = Column(String, default='0001')
    numero_conta = Column(Integer, autoincrement=True)
    saldo = Column(Float, default=0)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))

    user = relationship("Cliente", back_populates="addresses")


engine = create_engine('sqlite://', echo=True, future=True)

Base.metadata.create_all(engine)

with Session(engine) as session:
    eduardo = Cliente(
        nome="Eduardo",
        cpf="12345678910",
        endereco="R. Joelma",
        addresses=[
            Conta(
                saldo=400
            )
        ]
    )

    maria = Cliente(
        nome="Maria",
        cpf="98765432101",
        endereco="Av. das Flores",
        addresses=[
            Conta(
                saldo=700
            )
        ]
    )

    joao = Cliente(
        nome="João",
        cpf="24681357920",
        endereco="R. da Praia",
        addresses=[
            Conta(
                saldo=550
            )
        ]
    )

    luana = Cliente(
        nome="Luana",
        cpf="13579246830",
        endereco="Av. dos Sonhos",
        addresses=[
            Conta(
                saldo=900
            )
        ]
    )

    pedro = Cliente(
        nome="Pedro",
        cpf="36925814740",
        endereco="R. da Amizade",
        addresses=[
            Conta(
                saldo=300
            )
        ]
    )

    isabela = Cliente(
        nome="Isabela",
        cpf="15935724650",
        endereco="Av. do Progresso",
        addresses=[
            Conta(
                saldo=600
            )
        ]
    )

    lucas = Cliente(
        nome="Lucas",
        cpf="98765432101",
        endereco="R. da Alegria",
        addresses=[
            Conta(
                saldo=750
            )
        ]
    )

    juliana = Cliente(
        nome="Juliana",
        cpf="25814736912",
        endereco="Av. da Felicidade",
        addresses=[
            Conta(
                saldo=450
            )
        ]
    )

    andre = Cliente(
        nome="André",
        cpf="74185296323",
        endereco="R. da Criatividade",
        addresses=[
            Conta(
                saldo=800
            )
        ]
    )

    camila = Cliente(
        nome="Camila",
        cpf="65432198734",
        endereco="Av. da Inovação",
        addresses=[
            Conta(
                saldo=350
            )
        ]
    )

    session.add_all([eduardo, maria, joao, luana, pedro,
                    isabela, lucas, juliana, andre, camila])

    session.commit()


session = Session(engine)

stmt = select(Cliente).where(Cliente.nome.in_(["Eduardo", "Juliana"]))

for cliente in session.scalars(stmt):
    print(cliente)
