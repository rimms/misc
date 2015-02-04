How to test
===========

1. Register config to Zookeeper
 ::

   $ jubaconfig -c write -f config.json -z localhost:2181 -t classifier -n test
2. Start ``jubaclassifier`` in Distributed-mode
 ::

   $ jubaclassifier -n test -z localhost:2181 -s 0 -i 0 -I 60

3. Run ``test.py``
 ::

   $ ./test.py
