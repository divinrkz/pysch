import schedule
import time


class Schedule:
    def start(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    def job(self):
        print('Running job')

    schedule.every(10).seconds.do(job)  # Run job every 10 seconds
    schedule.every(10).minutes.do(job)  # Run job every 10 minutes
    schedule.every().hour.do(job)  # Run job every hour
    schedule.every().day.at("10:30").do(job)  # Run job every day at 10:30
    schedule.every(5).to(10).minutes.do(job)  # Run job every 5 to 10 minutes
    schedule.every().monday.do(job)  # Run job every monday
    schedule.every().wednesday.at("13:15").do(job)  # Run job every wednesday at 13:15
    schedule.every().minutes.at(":17").do(job)  # Run job every minutes at 17 seconds
    schedule.every().week.do(job)  # Run job every week
