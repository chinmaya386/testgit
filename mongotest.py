import pymongo

client = pymongo.MongoClient("mongodb+srv://chinmaya386:adiyogi@chinu.chfq6nu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"chinmaya",
    "email" : "chinmaya386@gmail.com",
    "surname" : "shankar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )




