print("Sinh viên: LÊ QUANG TRUNG")
print("Mã số SV: 23575202161012")

import datetime as dt

format = '%Y-%m-%dT%H:%M:%S'

t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

print('Day:', t1.day)
print('Month:', t1.month)
print('Minute:', t1.minute)
print('Second:', t1.second)

t2 = dt.datetime.now()

diff = t2 - t1

print('How many days difference?', diff.days)
