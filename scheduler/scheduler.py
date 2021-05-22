import schedule
import time


class Schedule:
    def __init__(self, job):
        print('Scheduler running ....')
        self.scheduler(job)

    def start(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    def scheduler(self, job):
        schedule.every().day.at("10:30").do(job)
        self.start()
