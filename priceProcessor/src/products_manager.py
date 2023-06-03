import logging

import pymongo

BRANCHES_COLLECTION = 'Branches'
CATEGORIES_COLLECTION = 'Categories'
PRODUCTS_COLLECTION = 'Products'
PRICES_COLLECTION = 'Prices'


class DomainManager:
    def __init__(self, db_client, db):
        self.db_client = db_client
        self.database = db
        self.branches = self.database[BRANCHES_COLLECTION]
        self.categories = self.database[CATEGORIES_COLLECTION]
        self.products = self.database[PRODUCTS_COLLECTION]
        self.prices = self.database[PRICES_COLLECTION]
        self.config_indexes()
        logging.info(f"DATA BASE OF MANAGER {self.database.name}")

    def config_indexes(self):
        self.branches.create_index("id", name='branch_index', unique=True)
        self.categories.create_index("name", name='category_index', unique=True)
        self.products.create_index("id", name='product_index', unique=True)
        logging.info(f"DATA BASE OF MANAGER2 {self.database.name}")
        self.prices.create_index(
            [("product_id", pymongo.ASCENDING), ("branch_id", pymongo.ASCENDING), ("date", pymongo.ASCENDING)],
            name='price_index', unique=True)
        logging.info(f"DATA BASE OF MANAGER3 {self.database.name}")

    def add(self, product):
        logging.info(f'Incoming product {product}')
        return {"inserted": 1}

    def add_branches(self, branches):
        logging.info(f'Incoming branches {len(branches)}  sample: {branches[0:10]}')
        result = self.branches.insert_many(branches)
        logging.info(f'Added branches {len(result.inserted_ids)}')
        return {"inserted": len(result.inserted_ids)}

    def add_categories(self, categories):
        logging.info(f'Incoming branches {len(categories)}  sample: {categories[0:10]}')
        result = self.categories.insert_many(categories)
        logging.info(f'Added branches {len(result.inserted_ids)}')
        return {"inserted": len(result.inserted_ids)}

    def add_product(self, products):
        logging.info(f'Incoming products {len(products)}  sample: {products[0:10]}')
        result = self.products.insert_many(products)
        logging.info(f'Added products {len(result.inserted_ids)}')
        return {"inserted": len(result.inserted_ids)}

    def add_price(self, prices):
        logging.info(f'Incoming prices {len(prices)}  sample: {prices[0:10]}')
        result = self.prices.insert_many(prices)
        logging.info(f'Added prices {len(result.inserted_ids)}')
        return {"inserted": len(result.inserted_ids)}


# -@app.route('/', methods=['POST'])
# -def handle_post():
# -    data = request.get_json()
# -    response = build_response(data)
# -    return response
# -
# -
# -def build_response(data):
# -    bulk_data = []
# -    for item in data:
# -        reduced = {
# -            "productName": get_product_name(item),
# -            "price": get_price(item),
# -            "EAN": get_ean(item)
#          }
# -        bulk_data.append(reduced)
# -    # Warn: each element gets a new ObjectId field '_id'. This field is not serializable by default.
# -    inserted = products_collection.insert_many(bulk_data)
# -    return {"inserted": len(inserted.inserted_ids)}
# -
# -
# -def get_product_name(product):
# -    return product["productName"]
# -
# -
# -def get_price(product):
# -    return product["priceRange"]["sellingPrice"]
# -
# -
# -def get_ean(product):
# -    specs_groups = product["specificationGroups"]
# -    group = next(group for group in specs_groups if group["name"] == "Especificaciones Genesix")
# -    ean_prop = next(prop for prop in group["specifications"] if prop["name"] == "EAN")
# -    return ean_prop["values"]
# -
# -
# -if __name__ == '__main__':
# -    app.run(host=host, port=port)
