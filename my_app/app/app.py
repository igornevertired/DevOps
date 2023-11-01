from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://mongo:27017/')
db = client.mydatabase

@app.route('/create', methods=['POST'])
def create():
    data = request.json
    db.mycollection.insert_one(data)
    return jsonify({"message": "Object created successfully"}), 201

@app.route('/update/<key>', methods=['PUT'])
def update(key):
    new_value = request.json.get('value')
    db.mycollection.update_one({"key": key}, {"$set": {"value": new_value}})
    return jsonify({"message": "Object updated successfully"}), 200

@app.route('/read/<key>', methods=['GET'])
def read(key):
    result = db.mycollection.find_one({"key": key}, {"_id": 0})
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"message": "Object not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
