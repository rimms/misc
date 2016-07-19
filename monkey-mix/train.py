#!/usr/bin/env python

import argparse
import random

from jubatus.classifier.client import Classifier
from jubatus.classifier.types import LabeledDatum
from jubatus.common import Datum


def parse_options():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-p', '--port',
    default  = 9199,
    type     = int,
    help     = 'Port Number',
    metavar  = 'PORT',
    dest     = 'port'
  )
  return parser.parse_args()


def main():
  args = parse_options()

  client = Classifier('127.0.0.1', args.port, 'test', 0)

  for i in range(0, 1000000):
    d = Datum()

    # Learn same data
    rand = random.randint(0, 1)
    d.add_number('key', 1.0 if rand else 2.0)
    ld = LabeledDatum('Pos' if rand else 'Neg', d)

    client.train([ld])

    if not i % 10000:
      print 'train ' + str(i) + ' data'


if __name__ == '__main__':
  main()
