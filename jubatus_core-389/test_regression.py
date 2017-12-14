import jubatus
from jubatus.common import Datum

import random

cl = jubatus.Regression('127.0.0.1', 9199, 'test', 0)

random.seed(1)
datum_length = 100

for i in range(3):
    d = Datum()
    for x in range(datum_length):
        d.add_number("{}".format(x), random.random())
    cl.train([(float(i), d)])

d = Datum()
for x in range(datum_length):
    d.add_number("{}".format(x), random.random())
cl.train([(3.0, d)])

cl.save('test')
cl.clear()
cl.load('test')  # should not be error

d = Datum()
for x in range(datum_length):
    d.add_number("{}".format(x), random.random())
cl.train([(4.0, d)])
print(cl.get_status())
