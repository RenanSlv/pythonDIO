import pprint
import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://pymongo:123aA456@cluster0.ida9hyx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.bank
collection = db.bank_collection
print(db.bank_collection)

post = [{
    "nome": "João",
    "cpf": "123456789",
    "endereco": "Rua ABC numero 123, bairro XYZ, cidade OK"
    },
    {
    "nome": "Marina",
    "cpf": "987654321",
    "endereco": "Rua CBA numero 31, bairro XYZ, cidade OK",
    "conta": {"tipo": "ContaCorrente",
              "agencia": "0001",
              "numero": "222",
              "saldo": "1500.50"}
    },
    {
    "nome": "Marcos",
    "cpf": "111222333",
    "endereco": "Rua CBA numero 456, bairro XYZ, cidade OK",
    "conta": {"tipo": "ContaPoupanca",
              "agencia": "0001",
              "numero": "333",
              "saldo": "5432.10"}
    }]

posts = db.posts
post_id = posts.insert_many(post)
print(post_id)
print(db.list_collection_names())


pprint.pprint(db.posts.find_one())
pprint.pprint(db.posts.find_one({"nome": "Marina"}))

print("\n\n")
print(posts.find())

print("\n Documentos presentes na coleção post\n")
for post in posts.find():
    pprint.pprint(post)

print("\nRecuperando info da coleção post de maneira ordenada\n")
for post in posts.find({}).sort("nome"):
    pprint.pprint(post)

print("\n\n")
print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {"nome": "Joaquim", "cpf": "999888777"},
    {"nome": "Maria Oliveira", "cpf": "555777333"}
]

result = db.posts.insert_many(user_profile_user)

print("\nColeções armazenadas no mongoDB\n")
collections = db.list_collection_names()
for collection in collections:
    print(collection)

for post in posts.find():
    pprint.pprint(post)
