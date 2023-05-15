import logging


class Products:
    def add(self, product):
        logging.info(f'Incoming product {product}')
        return {"inserted": 1}
