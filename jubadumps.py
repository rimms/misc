#!/usr/bin/env python

import argparse
import glob
import os
import json
from datetime import datetime


def parse_options():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-i',
    help     = 'Jubadump output File',
    metavar  = 'FILE',
    default  = '/dev/stdin',
    dest     = 'input'
  )
  return parser.parse_args()

def main():
  args = parse_options()

  with open(args.input) as f:
    data = json.loads(f.read())

  for k in data['storage']['weight'].keys():
    feature_name = k.encode('UTF-8')
    weights = data['storage']['weight'][k]
    weight_strs = []
    for l in weights.keys():
      label_name = l.encode('UTF-8')
      weight = weights[l]['v1']
      weight_str = label_name + ' = ' + str(weight)
      weight_strs.append(weight_str)

    print feature_name + ':', ', '.join(weight_strs)


if __name__ == '__main__':
    main()
