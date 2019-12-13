from flask import Flask, jsonify
from pymongo import MongoClient
import unittest

mongo= MongoClient('mongodb+srv://Test:test@cluster1-6nftz.mongodb.net/test?retryWrites=true&w=majority')

#creating client

app = Flask(__name__)
ab = mongo.get_database("database")
collection = ab.data

@app.route('/')
def  main():
    return 'Hello World'

#get api

@app.route('/getdata', methods= ['GET'])
def Getalldata():
    data = collection.find()
    ls = []
    print(type(data))
    for i in data:
        i.pop('_id')
        ls.append(i)
    return jsonify(ls)

    #GET API FOR SINGLE RECORD
@app.route('/GETSINGLEDATA/<idx>', methods= ['GET']) 
def GetSingleData(idx):
    x = collection.find_one({"id": idx})
    data = {}
    for i, v in x.items():
        if i != '_id':
            data[i] = v
    print(data)
    return jsonify(data)

#POST API
@app.route('/POSTDATA/<id>/<title>/<desc>/<done>', methods= ["POST"])
def POSTDATA(id, title, desc, done):
    data = {
        'id' : id,
        "title" : title,
        'description': desc,
        "done": done
    }


if __name__ == "__main__":
    app.run(debug= True)

