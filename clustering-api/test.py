#!/usr/bin/env python
# coding: utf-8

host = '127.0.0.1'
port = 9199
name = 'test'

import jubatus
from jubatus.common import Datum


def make_datum():
    d = Datum()
    d.add_string('string-key',   'str')
    d.add_number('number-key',     1.0)
    d.add_binary('binary-key',  b'bin')
    return d


if __name__ == '__main__':
    client = jubatus.Clustering(host, port, name)

    # push points
    for i in range(15):
        client.push([make_datum()])

    print ('get_revision => {}'.format(client.get_revision()))

    print ('get_nearest_center => {}'.format(client.get_nearest_center(make_datum())))

    print ('get_k_center => {}'.format(', '.join(list(map(str, client.get_k_center())))))

    print ('get_core_members => {}'.format(client.get_core_members()))

    print ('get_nearest_members =>'.format(client.get_nearest_members(make_datum())))
