#!/usr/bin/env python3
import logging
import os
import time
from threading import Thread
from src.scrapper import Scrapper
from src.scheduleTask import ScheduleTask
from src.server import SimpleServer

SCHEDULE_HOUR = 18
SCHEDULE_MIN = 55
HOST = 'localhost'
PORT = 8008

processor = os.environ['PROCESSOR_HOST']

print(os.environ.items())

def initialize_log():
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
    )


def main():
    initialize_log()
    try:
        logging.info("Initializing... ")
        # threads = []
        gov = Scrapper(f"http://{processor}:5000/products")
        # gov.scrap()
        # gov.send_data()

        sch = ScheduleTask()
        sch.daily_run_at(gov.send_data, SCHEDULE_HOUR, SCHEDULE_MIN)
        # threads.append(Thread(target=sch.daily_run_at, args=(schedule_task, SCHEDULE_HOUR, SCHEDULE_MIN)))
        server = SimpleServer(HOST, PORT)
        serverThread = Thread(target=server.run)
        # threads.append(Thread(target=server.run))
        serverThread.start()

        # for thread in threads:
        #     thread.start()
        logging.info("server runnig... ")

        # for thread in threads:
        #     # only move on when this thread finished
        serverThread.join()
        # threads.append(Thread(target=, args=(stop_event, shared_block_to_mine, start_mining_event, new_block_event)))
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        sch.shutdown()
        server.close()
    except Exception as error:
        logging.error("Something Wrong in main function: " + error.args)


if __name__ == "__main__":
    main()
