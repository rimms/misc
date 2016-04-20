#!/usr/bin/env python

from jubatus.classifier.client import Classifier

client = Classifier('127.0.0.1', 9000, 'test', 0)
client.do_mix()
