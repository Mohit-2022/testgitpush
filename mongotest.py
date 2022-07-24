import pymongo
client = pymongo.MongoClient("mongodb+srv://Ineuron:Ineuron2022@cluster0.lx5ca.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
     'name' : 'sudanshu',
    'email' : 'sudanshu@ineuron.ai',
    'surname' : 'kumar'
}
db1 = client ['mongotest']
coll =db1['test']
coll.insert_one(d)