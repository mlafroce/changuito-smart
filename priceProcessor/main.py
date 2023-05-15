import logging
import os
from threading import Thread

from src.products_manager import Products
from src.server import Server


# from pymongo import MongoClient


def load_envs_config():
    return {
        'server': {
            'host': os.environ.get('HOST', '0.0.0.0'),
            'port': int(os.environ.get('PORT', 5000))
        },
        'db': {
            'url': os.environ.get('MONGO_SERVER_URL', ''),
            'user': os.environ.get('MONGO_SERVER_USER', ''),
            'pass': os.environ.get('MONGO_SERVER_PASS', ''),
        }
    }


# def db_setup():
#     print(f"Connecting to {MONGO_SERVER_URL}")
#     mongo_client = MongoClient(MONGO_SERVER_URL, username=MONGO_SERVER_USER, password=MONGO_SERVER_PASS);
#     changuito_db = mongo_client["changuito"]
#     products_collection = changuito_db["products"]


def initialize_log():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
    )


def main():
    initialize_log()
    try:
        configs = load_envs_config()
        # db_setup()
        logging.info("DB runnig... ")
        productManager = Products()
        logging.info("Products() created... ")
        host, port = configs.get('server').values()
        server = Server(host, port, productManager)
        logging.info(" Server(port, host, productManager) created... ")
        serverThread = Thread(target=server.run)
        serverThread.start()
        logging.info("Server runnig... ")
        serverThread.join()
    except Exception as error:
        logging.error(f'Something is wrong in main function {error}')


if __name__ == "__main__":
    main()
