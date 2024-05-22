import os
from flask import Flask, jsonify, request, render_template, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Konfigurácia MongoDB
mongo_url = os.getenv("DATABASE_URL", "mongodb://db:27017/mydatabase")
client = MongoClient(mongo_url)
db = client.mydatabase

@app.route('/')
def index():
    items = list(db.items.find({}, {'_id': False}))
    return render_template('index.html', items=items)

@app.route('/data', methods=['POST'])
def add_data():
    item = request.form.get('item')
    if item:
        db.items.insert_one({'item': item})
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_data():
    item = request.form.get('item')
    if item:
        db.items.delete_one({'item': item})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
