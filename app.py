import os
from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Konfigurácia MongoDB
mongo_url = os.getenv("DATABASE_URL", "mongodb://db:27017/mydatabase")
client = MongoClient(mongo_url)
db = client.mydatabase

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        item = request.json
        db.items.insert_one(item)
        return jsonify(item), 201
    else:
        items = list(db.items.find({}, {'_id': False}))
        return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)