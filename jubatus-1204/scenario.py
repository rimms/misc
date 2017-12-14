import random
import time

import jubatus
from jubatus.common import Datum


HOST="127.0.0.1"
PORT_P=9199
PORT_1=19199
PORT_2=19200
NAME="test"


def generate_data(num = 10, mu = 1.0, sigma = 1.0):
    res = []
    for i in range(num):
        x = random.gauss(mu, sigma)
        y = random.gauss(mu, sigma)
        z = random.gauss(mu, sigma)
        res.append((x, y, z))
    return res

def add_data(num = 10):
    data = generate_data(num)
    client = jubatus.Anomaly(HOST, PORT_P, NAME)
    for d in data:
        dt = Datum({"x": d[0],
                    "y": d[1],
                    "z": d[2]})
        result = client.add(dt)
        print('Added {0}, score = {1}'.format(result.id, result.score))

def print_rows(port):
    client = jubatus.Anomaly(HOST, port, NAME)
    rows = client.get_all_rows()
    print(' - ID in {0}: {1}'.format(port, ' '.join(sorted(rows, key=int))))

def print_all_rows():
    print_rows(PORT_1)
    print_rows(PORT_2)

def do_mix(sleep_sec = 3.0):
    client = jubatus.Anomaly(HOST, PORT_1, NAME)
    client.do_mix()
    print('Do MIX and wait {0} sec'.format(sleep_sec))
    time.sleep(sleep_sec)

def clear():
    client = jubatus.Anomaly(HOST, PORT_P, NAME)
    client.clear()

def main():
    clear()
    for i in range(30):
        add_data(1)
        print_all_rows()
        do_mix()
        print_all_rows()

if __name__ == "__main__":
    main()
