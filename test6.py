



from datetime import datetime, timedelta
past = datetime.now() - timedelta(days = 1)
now = datetime.now()
print(now)
print(past)

present = datetime.now()
print(past < present)
