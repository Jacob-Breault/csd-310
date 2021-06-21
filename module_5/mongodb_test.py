#Jacob Breault
#6/20/2021
#Module 5.2 Assignment
#Purpose: How to connect test
from pymongo import MongoClient

#This here is how you connect.
url = "mongodb+srv://admin:admin@cluster0.kseok.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

#Create a variable named client and call the MongoClient passing-in the url variable.
client = MongoClient(url)

#Create a variable named db and assign it to the pytech database instance.
db = client.pytech

#Output collection.
print(" -- PyTech COllection List --")
print(db.list_collection_names())

input("End of program, press any key to exit...")
