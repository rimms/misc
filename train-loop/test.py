#!/usr/bin/env python

import random
import time

from jubatus.classifier.client import Classifier
from jubatus.classifier.types import LabeledDatum
from jubatus.common import Datum

data = []
for i in xrange(0, 100000):
  d = Datum()
  for j in xrange(0, 20):
    d.add_number(str(j) + '-' + str(i), random.random() + 1.0)

  ld = LabeledDatum('Pos' if random.randint(0, 1) else 'Neg', d)
  data.append(ld)

client = Classifier('127.0.0.1', 9199, 'test', 0)


start_time = time.time()
client.train(data)
end_time = time.time()

print str(len(data)) + ' ... ' + str((end_time - start_time) * 1000) + ' msec'
