import logging
import os
import time
from threading import Thread

from pymongo import MongoClient

from src.products_manager import DomainManager
from src.server import Server


def load_envs_config():
    return {
        'server': {
            'host': os.environ.get('HOST', '0.0.0.0'),
            'port': int(os.environ.get('PORT', 5000))
        },
        'db_client': {
            'url': os.environ.get('MONGO_SERVER_URL', ''),
            'user': os.environ.get('MONGO_SERVER_USER', ''),
            'pass': os.environ.get('MONGO_SERVER_PASS', ''),
            'database': os.environ.get('MONGO_DATABASE', 'changuito')
        }
    }


def initialize_log():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
    )


def main():
    initialize_log()
    try:
        time.sleep(3)
        configs = load_envs_config()
        url, usr, password, database = configs.get('db_client').values()
        db_client = MongoClient(url, username=usr, password=password)
        db = db_client[database]
        logging.info("DB runnig... ")
        productManager = DomainManager(db_client, db)
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

