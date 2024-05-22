from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

from bson import json_util, ObjectId
import json

app = Flask(__name__)

# Konfigurácia MongoDB
client = MongoClient("mongodb://db:27017")
db = client.mydatabase

@app.route('/')
def index():
    items = list(db.items.find({}, {'_id': True, 'name': True, 'description': True}))
    for item in items:
        item['_id'] = str(item['_id'])  # Konvertuje ObjectId na string
    return render_template('index.html', items=items)

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        item = request.json
        result = db.items.insert_one(item)
        # Pridajte tu konverziu ObjectId na string
        item['_id'] = str(result.inserted_id)
        return jsonify(item), 201
    else:
        # Tu použite json_util pri čítaní položiek na konverziu ObjectId na string
        items = list(db.items.find({}, {'_id': False}))
        return json.dumps(items, default=json_util.default)
        return jsonify(items)
        
@app.route('/remove/<item_id>', methods=['POST'])
def remove_item(item_id):
    db.items.delete_one({'_id': ObjectId(item_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
