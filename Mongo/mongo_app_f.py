from flask import Flask
import pymongo

app = Flask(__name__)

# this is the handler for the default path of the web server

@app.route('/')
def index():
    
    # connect to mongoDB
    connection = pymongo.MongoClient('localhost', 27017)

    # attach to test database
    db = connection.test

    # get handle for names collection
    name = db.names

    # find a single document
    item = name.find_one()

    return '<b>Hello %s!</b>' % item['name']

if __name__ == '__main__':
	app.run(host='localhost', port=8082)
