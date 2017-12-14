import jubatus
from jubatus.common import Datum

import random

cl = jubatus.Classifier('127.0.0.1', 9199, 'test', 0)

random.seed(1)
datum_length = 100

for i in range(3):
    d = Datum()
    for x in range(datum_length):
        d.add_number("{}".format(x), random.random())
    cl.train([(str(i), d)])

print('labels:{}'.format(','.join(cl.get_labels())))  # 1, 2, 3

d = Datum()
for x in range(datum_length):
    d.add_number("{}".format(x), random.random())
cl.train([('3', d)])
print('labels:{}'.format(','.join(cl.get_labels())))  # unlearn 1 label

cl.save('test')
cl.clear()
cl.load('test')

print('labels:{}'.format(','.join(cl.get_labels())))  # should be same as before `save`

d = Datum()
for x in range(datum_length):
    d.add_number("{}".format(x), random.random())
cl.train([('4', d)])
print('labels:{}'.format(','.join(cl.get_labels())))  # unlearn 1 label
