from flask import Flask, request
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

connection = MongoClient(
    'mongodb+srv://de_saurabh:powerrangersgo@gabrieldb001.feuqz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = connection['todo']
collections = db['list']

# collections.insert_one({"_id": 0, "_item": "Learn Flask", "_owner": "saurabh", "_isDone": 'false'})
# collections.delete_one({"_id": 0})
# collections.insert_one({"_id": 0, "_item": "Learn Flask", "_owner": "saurabh", "_isDone": 'false'})
# collections.insert_one({"_id": 1, "_item": "Learn Python", "_owner": "saurabh", "_isDone": 'false'})
# collections.insert_one({"_id": 2, "_item": "Learn MongoDB", "_owner": "saurabh", "_isDone": 'false'})
# collections.insert_one({"_id": 3, "_item": "Learn Cassandra", "_owner": "saurabh", "_isDone": 'false'})
# collections.insert_one({"_id": 4, "_item": "Learn PyCharm", "_owner": "saurabh", "_isDone": 'false'})
#
# item5 = {"_id": 5, "_item": "Learn Python Loops", "_owner": "saurabh", "_isDone": 'false'}
# item6 = {"_id": 6, "_item": "Learn Python Conditionals", "_owner": "saurabh", "_isDone": 'false'}
#
# collections.insert_many([item5, item6])

app = Flask(__name__)


@app.route('/list', methods=['GET'])
def get_todo_items():
    all_items = list(collections.find({}))
    return json.dumps(all_items, default=json_util.default)


@app.route('/add_item', methods=['POST'])
def add_todo_item():
    request_payload = request.json
    list_item = request_payload['list_item']
    collections.insert_one({"_id": list_item['id'], "_item": list_item['item'], "_owner": list_item['owner'], "_isDone": list_item['isDone']})
    # collections.insert_one({"_id": 44, "_item": "Learn PyCharm", "_owner": "saurabh", "_isDone": 'false'})
    return 'Item has been added successfully!!!'


