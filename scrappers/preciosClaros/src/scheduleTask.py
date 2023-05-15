import datetime as dt
import logging
from apscheduler.schedulers.background import BackgroundScheduler


class ScheduleTask:
    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def daily_run_at(self, task, hour, minute):
        logging.info("1 Task has been set")
        # self.scheduler.add_job(task, 'cron', hour=hour, minute=minute)
        self.scheduler.add_job(task, 'interval', seconds=10)
        self.scheduler.start()
        logging.info(self.scheduler)
        logging.info("2 Task has been set")

    def shutdown(self):
        self.scheduler.shutdown()
