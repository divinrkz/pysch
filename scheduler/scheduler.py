import schedule
import time


class Schedule:
    def __init__(self, ):
        schedule.every().day.at("10:30").do(job)  # Run job every day at 10:30

    def start(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

