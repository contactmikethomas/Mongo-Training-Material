import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {"firstname":"Data","lastname":"Exploitation"}
print doc
print "about to insert document"

try:
	users.insert_one(doc)
except Exception as e:
	print "insert failed", e

print doc
print "inserting again"
doc = {"firstname":"Data","lastname":"Exploitation"}

try:
	users.insert_one(doc)
except Exception as e:
	print "second insert failed", e

print doc

