import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/NishuLab')

database = client['NishuLab']
collection = database['Products']


d = {
    'CompanyName': 'NishuLab',
    'Product': 'Affordable Ai',
    'Service Offered': 'Chatbot with simple task handling'
}

rec = collection.insert_one(d)

all_rec = collection.find()

for idx, record in enumerate(all_rec):
    print(f'{idx}: {record}')