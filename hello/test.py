from datetime import datetime

date_str = datetime.utcnow().strftime('%Y%m%d')
time_str = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
print("task ", date_str, time_str)
