from scheduler.scheduler import Schedule
from db.jobs.jobs import Jobs

schedule = Schedule(job=Jobs.update_instance, _collection='tokens', _prop='status', _val=1, _dict={})

