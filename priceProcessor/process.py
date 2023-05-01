import os
from flask import Flask, jsonify, request
from pymongo import MongoClient

MONGO_SERVER_URL = os.environ['MONGO_SERVER_URL']
MONGO_SERVER_USER = os.environ['MONGO_SERVER_USER']
MONGO_SERVER_PASS = os.environ['MONGO_SERVER_PASS']

print(f"Connecting to {MONGO_SERVER_URL}")
mongo_client = MongoClient(MONGO_SERVER_URL, username=MONGO_SERVER_USER, password=MONGO_SERVER_PASS);

changuito_db = mongo_client["changuito"]
products_collection = changuito_db["products"]

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    data = request.get_json()
    response = build_response(data)
    return response

def build_response(data):
    bulk_data = []
    for item in data:
        reduced = {
            "productName": get_product_name(item),
            "price": get_price(item),
            "EAN": get_ean(item)
        }
        bulk_data.append(reduced)
    # Warn: each element gets a new ObjectId field '_id'. This field is not serializable by default.
    inserted = products_collection.insert_many(bulk_data)
    return {"inserted": len(inserted.inserted_ids)}

def get_product_name(product):
    return product["productName"]

def get_price(product):
    return product["priceRange"]["sellingPrice"]

def get_ean(product):
    specs_groups = product["specificationGroups"]
    group = next(group for group in specs_groups if group["name"] == "Especificaciones Genesix")
    ean_prop = next(prop for prop in group["specifications"] if prop["name"] == "EAN")
    return ean_prop["values"]

if __name__ == '__main__':
    app.run()
