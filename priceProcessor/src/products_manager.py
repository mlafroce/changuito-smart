import logging


class Products:
    def __init__(self, db_client):
        self.db = db_client

    def add(self, product):
        logging.info(f'Incoming product {product}')
        return {"inserted": 1}
