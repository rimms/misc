#!/usr/bin/env python

from jubatus.classifier.client import Classifier


client = Classifier('127.0.0.1', 9199, 'test')

for i in range(0, 10000):
  client.do_mix()
  if not i % 100:
    status = client.get_status()
    for node in status.keys():
      print '\t'.join([str(i), node, status[node]['RSS']])
