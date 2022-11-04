import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://yuliana:ipxr0s9g3QPPMJSD@mintic4.ktjkavc.mongodb.net/results_db?retryWrites=true&w=majority",
    tlsCAFile=ca
)
db = client.test

print(db)

data_base = client['results_db']
print(data_base.list_collection_names())

candidate = data_base.get_collection('candidate')
all_candidate = candidate.find({})

political_party = data_base.get_collection('political_party')
all_political_parties = political_party.find('political_parties')
