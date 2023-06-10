import logging
import os
import time
from threading import Thread

from pymongo import MongoClient

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
            'database': os.environ.get('MONGO_DATABASE', 'changuito'),
            # 'conn_str': os.environ.get('MONGO_SERVER_CONNECTION_STRING', ''),
        },
        'elastic_client': {
            'url': os.environ.get('ELASTICSEARCH_URL', '')
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
    logging.info("after sleep")

    # try:
    time.sleep(25)
    logging.info("after sleep")
    configs = load_envs_config()
    logging.info("after envs config")
    url, usr, password, database = configs.get('db_client').values()
    db_client = MongoClient(url, username=usr, password=password)
    db = db_client[database]
    logging.info("DB runnig... ")
    elastic_url = configs.get('elastic_client').get('url')
    host, port = configs.get('server').values()
    server = Server(host, port, db, elastic_url)

    logging.info(" Server created... ")
    serverThread = Thread(target=server.run)
    serverThread.start()
    logging.info("Server runnig... ")
    serverThread.join()

# except Exception as error:
#     logging.error(f'Something is wrong in main function {error}')


if __name__ == "__main__":
    main()