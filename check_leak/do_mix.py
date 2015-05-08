#!/usr/bin/env python

from jubatus.classifier.client import Classifier


client = Classifier('127.0.0.1', 9199, 'test')

for i in xrange(0, 10000):
  client.do_mix()
