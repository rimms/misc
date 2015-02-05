How to test
===========

1. Register config to Zookeeper

.. code-block:: bash

   $ jubaconfig -c write -f config.json -z localhost:2181 -t classifier -n test

2. Start ``jubaclassifier`` in Distributed-mode

.. code-block:: bash

   $ jubaclassifier -n test -z localhost:2181 -s 0 -i 0 -I 60

3. Run ``test.py``

.. code-block:: bash

   $ ./test.py
