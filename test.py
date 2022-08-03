import pymongo
import urllib

client = pymongo.MongoClient("mongodb+srv://Slkpddm:"+urllib.parse.quote("Slkpddm8@")+"@cluster0.mrxuk.mongodb.net/?retryWrites=true&w=majority")
db = client.test

#Creating a database
db1=client["skp"]

#Creating a collection inside a database
collection1 = db1["test"]

#Now we will insert some record inside collection
record = {"name":"Super_Star-SKP" , "ID":"R141038" , "State":"Andra Pradesh"}
collection1.insert_one(record)


