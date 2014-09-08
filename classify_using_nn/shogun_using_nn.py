#!/usr/bin/env python
# -*- coding: utf-8 -*-

host = '127.0.0.1'
port = 9199
name = 'test'

import sys
import json
import random

import jubatus
from jubatus.common import Datum

def train(client):
    client.set_row(u'徳川01', Datum({'name': u'家康'}))
    client.set_row(u'徳川02', Datum({'name': u'秀忠'}))
    client.set_row(u'徳川03', Datum({'name': u'家光'}))
    client.set_row(u'徳川04', Datum({'name': u'家綱'}))
    client.set_row(u'徳川05', Datum({'name': u'綱吉'}))
    client.set_row(u'徳川06', Datum({'name': u'家宣'}))
    client.set_row(u'徳川07', Datum({'name': u'家継'}))
    client.set_row(u'徳川08', Datum({'name': u'吉宗'}))
    client.set_row(u'徳川09', Datum({'name': u'家重'}))
    client.set_row(u'徳川10', Datum({'name': u'家治'}))
    client.set_row(u'徳川11', Datum({'name': u'家斉'}))
    client.set_row(u'徳川12', Datum({'name': u'家慶'}))
    client.set_row(u'徳川13', Datum({'name': u'家定'}))
    client.set_row(u'徳川14', Datum({'name': u'家茂'}))

    client.set_row(u'足利01', Datum({'name': u'尊氏'}))
    client.set_row(u'足利02', Datum({'name': u'義詮'}))
    client.set_row(u'足利03', Datum({'name': u'義満'}))
    client.set_row(u'足利04', Datum({'name': u'義持'}))
    client.set_row(u'足利05', Datum({'name': u'義量'}))
    client.set_row(u'足利06', Datum({'name': u'義教'}))
    client.set_row(u'足利07', Datum({'name': u'義勝'}))
    client.set_row(u'足利08', Datum({'name': u'義政'}))
    client.set_row(u'足利09', Datum({'name': u'義尚'}))
    client.set_row(u'足利10', Datum({'name': u'義稙'}))
    client.set_row(u'足利11', Datum({'name': u'義澄'}))
    client.set_row(u'足利12', Datum({'name': u'義稙'}))
    client.set_row(u'足利13', Datum({'name': u'義晴'}))
    client.set_row(u'足利14', Datum({'name': u'義輝'}))
    client.set_row(u'足利15', Datum({'name': u'義栄'}))

    client.set_row(u'北条01', Datum({'name': u'時政'}))
    client.set_row(u'北条02', Datum({'name': u'義時'}))
    client.set_row(u'北条03', Datum({'name': u'泰時'}))
    client.set_row(u'北条04', Datum({'name': u'経時'}))
    client.set_row(u'北条05', Datum({'name': u'時頼'}))
    client.set_row(u'北条06', Datum({'name': u'長時'}))
    client.set_row(u'北条07', Datum({'name': u'政村'}))
    client.set_row(u'北条08', Datum({'name': u'時宗'}))
    client.set_row(u'北条09', Datum({'name': u'貞時'}))
    client.set_row(u'北条10', Datum({'name': u'師時'}))
    client.set_row(u'北条11', Datum({'name': u'宗宣'}))
    client.set_row(u'北条12', Datum({'name': u'煕時'}))
    client.set_row(u'北条13', Datum({'name': u'基時'}))
    client.set_row(u'北条14', Datum({'name': u'高時'}))
    client.set_row(u'北条15', Datum({'name': u'貞顕'}))

def predict(client):
    # predict the last shogun
    data = [
        Datum({'name': u'慶喜'}),
        Datum({'name': u'義昭'}),
        Datum({'name': u'守時'}),
    ]
    for d in data:
        res = client.neighbor_row_from_datum(d, 10)
        # get the predicted shogun name
        scores = {}
        for x in res:
          if scores.has_key(x.id.decode('utf-8')[0:2]):
            scores[x.id.decode('utf-8')[0:2]] += x.score
          else:
            scores[x.id.decode('utf-8')[0:2]] = x.score
        sys.stdout.write(max(scores, key = scores.get))
        sys.stdout.write(' ')
        sys.stdout.write(d.string_values[0][1].encode('utf-8'))
        sys.stdout.write('  ... ')
        for k in scores.keys():
            sys.stdout.write(' ' + k + '=' + str(scores[k]))
        sys.stdout.write('\n')

if __name__ == '__main__':
    # connect to the jubatus
    client = jubatus.NearestNeighbor(host, port, name)
    # run example
    train(client)
    predict(client)

