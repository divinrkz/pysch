import schedule
import time


class Schedule:
    def __init__(self, job, **kwargs):
        self.job = job
        self.args = kwargs
        print('Scheduler running ...')
        self.scheduler(self.fn)

    def start(self):
        print('start')
        while True:
            schedule.run_pending()
            time.sleep(1)

    def fn(self):
        print(self.args)
        self.job(self.args['_collection'], self.args['_prop'], self.args['_val'], self.args['_dict'])

    def scheduler(self, job):
        schedule.every(10).seconds.do(job)
        # schedule.every().day.at("10:30").do(job)
        self.start()
