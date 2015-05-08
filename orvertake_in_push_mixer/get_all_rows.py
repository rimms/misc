#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
from jubatus.recommender.client import Recommender

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)

def parse_options():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-t',
    help     = 'hostname',
    metavar  = 'HOST',
    default  = '127.0.0.1',
    dest     = 'host'
  )
  parser.add_argument(
    '-n',
    help     = 'cluster-name',
    metavar  = 'NAME',
    default  = 'test',
    dest     = 'name'
  )
  parser.add_argument(
    '-p',
    help     = 'ports',
    nargs    = '*',
    metavar  = 'PORT',
    default  = [9199],
    dest     = 'ports'
  )
  return parser.parse_args()


def main():
  args = parse_options()

  for port in args.ports:
    client = Recommender(args.host, int(port), args.name)
    try:
      result = client.get_all_rows()
      logging.info('{0}:{1} ... {2}'.format(args.host, port, result))
    except:
      logging.exception('{0}:{1}'.format(args.host, port))


if __name__ == '__main__':
    main()
