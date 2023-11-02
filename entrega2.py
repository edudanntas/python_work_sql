from pymongo.mongo_client import MongoClient
from pymongo import MongoClient
from decouple import config

uri = config('URI')

client = MongoClient(uri)

db = client['bank_databse']

bank_collection = db['bank']

clientes = [
    {
        "nome": "Eduardo",
        "cpf": "12345678910",
        "endereco": "R. Joelma",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "0001",
                "numero_conta": 1,
                "saldo": 400
            }
        ]
    },
    {
        "nome": "Maria",
        "cpf": "98765432101",
        "endereco": "Av. das Flores",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "0001",
                "numero_conta": 2,
                "saldo": 700
            }
        ]
    },
    {
        "nome": "Paulo",
        "cpf": "11122334455",
        "endereco": "R. das Rosas",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "0002",
                "numero_conta": 3,
                "saldo": 550
            }
        ]
    },
    {
        "nome": "Amanda",
        "cpf": "22233445566",
        "endereco": "Av. da Liberdade",
        "contas": [
            {
                "tipo": "Conta Poupança",
                "agencia": "0003",
                "numero_conta": 4,
                "saldo": 950
            }
        ]
    },
    {
        "nome": "Ricardo",
        "cpf": "33344556677",
        "endereco": "R. do Sol",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "0001",
                "numero_conta": 5,
                "saldo": 300
            }
        ]
    },
    {
        "nome": "Patrícia",
        "cpf": "44455667788",
        "endereco": "Av. Central",
        "contas": [
            {
                "tipo": "Conta Poupança",
                "agencia": "0004",
                "numero_conta": 6,
                "saldo": 750
            }
        ]
    },
    {
        "nome": "Luciano",
        "cpf": "55566778899",
        "endereco": "R. dos Pássaros",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "0002",
                "numero_conta": 7,
                "saldo": 600
            }
        ]
    },
    {
        "nome": "Camila",
        "cpf": "66677889900",
        "endereco": "Av. das Estrelas",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "0001",
                "numero_conta": 8,
                "saldo": 850
            }
        ]
    },
    {
        "nome": "Thiago",
        "cpf": "77788990011",
        "endereco": "R. da Lua",
        "contas": [
            {
                "tipo": "Conta Poupança",
                "agencia": "0005",
                "numero_conta": 9,
                "saldo": 500
            }
        ]
    },
    {
        "nome": "Isabel",
        "cpf": "88899001122",
        "endereco": "Av. dos Sonhos",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "0003",
                "numero_conta": 10,
                "saldo": 400
            }
        ]
    },
    {
        "nome": "Felipe",
        "cpf": "99900112233",
        "endereco": "R. da Alegria",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "0001",
                "numero_conta": 11,
                "saldo": 700
            }
        ]
    },
    {
        "nome": "Renata",
        "cpf": "11122334455",
        "endereco": "Av. das Flores",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "0001",
                "numero_conta": 12,
                "saldo": 550
            }
        ]
    },
    {
        "nome": "Gustavo",
        "cpf": "22233445566",
        "endereco": "R. das Árvores",
        "contas": [
            {
                "tipo": "Conta Poupança",
                "agencia": "0002",
                "numero_conta": 13,
                "saldo": 850
            }
        ]
    },
    {
        "nome": "Larissa",
        "cpf": "33344556677",
        "endereco": "Av. Central",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "0001",
                "numero_conta": 14,
                "saldo": 600
            }
        ]
    },
    {
        "nome": "André",
        "cpf": "44455667788",
        "endereco": "R. dos Pássaros",
        "contas": [
            {
                "tipo": "Conta Corrente",
                "agencia": "0003",
                "numero_conta": 15,
                "saldo": 450
            }
        ]
    }
]


bank_collection.insert_many(clientes)


resultado = bank_collection.find_one({"cpf": '12345678910'})
print(resultado)


nome_busca = "Eduardo"
resultado = bank_collection.find_one({"nome": nome_busca})

if resultado:
    contas = resultado.get("contas")
    for conta in contas:
        print(conta)
