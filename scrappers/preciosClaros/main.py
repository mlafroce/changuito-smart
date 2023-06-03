#!/usr/bin/env python3
import logging
import os
import time
from threading import Thread

# from src.scrapper import BaseScrapper
from src.scrappers import PriceScrapper
from src.server import SimpleServer

SCHEDULE_HOUR = 18
SCHEDULE_MIN = 55
HOST = 'localhost'
PORT = 8008

# get envs
processor_host = os.environ['PROCESSOR_HOST']
procesor_port = int(os.environ['PROCESSOR_PORT'])
post_endpoints = {
    "products": os.environ['PROCESSOR_POST_PRODUCT'],
    "prices": os.environ['PROCESSOR_POST_PRICE'],
    "categories": os.environ['PROCESSOR_POST_CATEGORIES'],
    "branches": os.environ['PROCESSOR_POST_BRANCHES']
}
url = os.environ['URL_TO_SCRAP']
endpoints = {
    "branches": os.environ['BRANCH_ENDPOINT'],
    "categories": os.environ['CATEGORY_ENDPOINT'],
    "products": os.environ['PRODUCTS_ENDPOINT']
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
        time.sleep(6)
        # branches_scrapper = BranchesScrapper(dst_url=f"http://{processor_host}:{procesor_port}",
        #                                      dst_endpoint=post_branches_endpoint,
        #                                      url=url, endpoint=endpoints["branches"], limit=30,
        #                                      domain=Branch, domain_encoder=DomainEncoder, name="BRANCHES"
        #                                      )
        # categories_scrapper = CategoriesScrapper(dst_url=f"http://{processor_host}:{procesor_port}",
        #                                          dst_endpoint=post_branches_endpoint,
        #                                          url=url, endpoint=endpoints["categories"], limit=100,
        #                                          domain=Category, domain_encoder=DomainEncoder, name="CATEGORIES"
        #                                          )
        # products_scrapper = ProductsScrapper(dst_url=f"http://{processor_host}:{procesor_port}",
        #                                      dst_endpoint=post_product_endpoint,
        #                                      url=url, endpoint=endpoints["products"], limit=100,
        #                                      domain=Product, domain_encoder=DomainEncoder, name="PRODUCTS",
        #                                      branch_scrapper=branches_scrapper, category_scrapper=categories_scrapper)
        prices_scrapper = PriceScrapper(dst_url=f"http://{processor_host}:{procesor_port}",
                                        dst_endpoints=post_endpoints,
                                        scrap_url=url, scrap_endpoints=endpoints, limit=100)

        prices_scrapper.scrap()

        # branches_scrapper.scrap()
        logging.info("Initializing... ")
        # gov = BaseScrapper(f"http://{processor_host}:5000")
        # # gov.scrap()
        # gov.send_data()
        # time.sleep(10)
        # gov.send_data()

        # sch = ScheduleTask()
        # sch.daily_run_at(gov.send_data, SCHEDULE_HOUR, SCHEDULE_MIN)
        server = SimpleServer(HOST, PORT)
        serverThread = Thread(target=server.run)
        serverThread.start()

        # for thread in threads:
        #     thread.start()
        logging.info("server runnig... ")

        # for thread in threads:
        #     # only move on when this thread finished
        serverThread.join()
        # threads.append(Thread(target=, args=(stop_event, shared_block_to_mine, start_mining_event, new_block_event)))
    # except (KeyboardInterrupt, SystemExit):
    #     # Not strictly necessary if daemonic mode is enabled but should be done if possible
    #     sch.shutdown()
    #     server.close()
    except Exception as error:
        logging.error(f"Something Wrong in main function: {error}")


if __name__ == "__main__":
    main()
