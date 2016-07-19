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

  for i in range(0, 10000):
    client.do_mix()

    if not i % 100:
      status = client.get_status()
      for node in status.keys():
        print '\t'.join([str(i), node, status[node]['RSS']])


if __name__ == '__main__':
  main()
