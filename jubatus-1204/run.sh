#!/bin/bash

NAME="test"

jubaconfig -c write -f light_lof_config.json -n "${NAME}" -t anomaly -z 127.0.0.1:2181 > /dev/null

jubaanomaly_proxy -z 127.0.0.1:2181 -p 9199 > /dev/null &
pid_p=$!

jubaanomaly -p 19199 -z 127.0.0.1:2181 -n "${NAME}" > /dev/null &
pid_1=$!

jubaanomaly -p 19200 -z 127.0.0.1:2181 -n "${NAME}" > /dev/null &
pid_2=$!

sleep 3s
if [ -z "${1}" ]; then
    python scenario.py
else
    python scenario.py | tee ${1}
fi

kill $pid_p $pid_1 $pid_2
