from scheduler.scheduler import Schedule
from db.jobs.job import Job

schedule = Schedule(job=Job.update_token)