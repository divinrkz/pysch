from scheduler.scheduler import Schedule
from db.jobs.jobs import Jobs

schedule = Schedule(job=Jobs.update_instance, _collection='tokens', _id='60a8c3dd7e5be48a6e414188', _dict={})

