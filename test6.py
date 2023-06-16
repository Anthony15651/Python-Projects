



from datetime import datetime, timedelta
past = datetime.now() - timedelta(days = 1)
print(past)

present = datetime.now()
print(past < present)
