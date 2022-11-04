import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
"mongodb+srv://jony:<Jony12345>@registraduria.juia4lh.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.test
print(db)

data_base = client.get_database('registraduria')
print(data_base)

collection = data_base.get_collection('table')
print(collection)


