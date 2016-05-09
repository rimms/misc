#!/usr/bin/env python

from jubatus.classifier.client import Classifier
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='(Thread-%(threadName)s) %(message)s',)

class SaveWorker(threading.Thread):
  def __init__(self, name, count):
    super(SaveWorker, self).__init__()
    self.name = name
    self.count = count

  def run(self):
    logging.debug('Start running with name: {0}, count: {1}'.format(self.name, self.count))
    client = Classifier('127.0.0.1', 9199, 'test')
    for i in range(0, self.count):
      client.save(self.name + str(i))
    logging.debug('Finished running')

if __name__ == '__main__':
  for i in range(0, 100):
    w = SaveWorker(str(i), 1000)
    w.start()
