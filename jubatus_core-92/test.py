#!/usr/bin/env python

from jubatus.anomaly.client import Anomaly
from jubatus.common import Datum


client = Anomaly('127.0.0.1', 9199, 'test')

for i in range(1, 21):
  d = Datum({'key': float(i)})
  client.add(d)
  print 'ids(' + str(i) + ') = ' + str(sorted(client.get_all_rows()))
