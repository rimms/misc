import jubatus
from jubatus.common import Datum

import random

cl = jubatus.Recommender('127.0.0.1', 9199, 'test', 0)

random.seed(1)
datum_length = 100

for i in range(3):
    d = Datum()
    for x in range(datum_length):
        d.add_number("{}".format(x), random.random())
    cl.update_row(str(i), d)

print('ids:{}'.format(','.join(cl.get_all_rows())))  # 1, 2, 3

d = Datum()
for x in range(datum_length):
    d.add_number("{}".format(x), random.random())
cl.update_row('3', d)
print('ids:{}'.format(','.join(cl.get_all_rows())))  # unlearn 1 id

cl.save('test')
cl.clear()
cl.load('test')

print('ids:{}'.format(','.join(cl.get_all_rows())))  # should be same as before `save`

d = Datum()
for x in range(datum_length):
    d.add_number("{}".format(x), random.random())
cl.update_row('4', d)
print('ids:{}'.format(','.join(cl.get_all_rows())))  # unlearn 1 id
