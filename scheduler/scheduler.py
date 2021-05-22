import schedule
import time


class Schedule:
    def __init__(self, job, **kwargs):
        self.job = job
        self.args = kwargs
        print('Scheduler running ...')
        self.scheduler(self.fn)

    def start(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    def fn(self):
        self.job(self.args['_name'], self.args['_collection'], self.args['_id'], self.args['_dict'])

    def scheduler(self, job):
        schedule.every().day.at("00:00").do(job)
        self.start()
