#!/usr/bin/env python

from jubatus.classifier.client import Classifier
import time

for idx in xrange(1, 50):
  time.sleep(600)
  client = Classifier('127.0.0.1', 9199, 'test')
  for i in xrange(1, 10001):
    client.do_mix()
    if not i % 1000:
      status = client.get_status()
      for node in status.keys():
        print '\t'.join([str((idx * 10000) + i ), node, status[node]['RSS']])
