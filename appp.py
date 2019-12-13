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
