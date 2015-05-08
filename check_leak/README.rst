How to test
===========

1. Register config to Zookeeper

.. code-block:: bash

   $ jubaconfig -c write -f config.json -z localhost:2181 -t classifier -n test

2. Start ``jubaclassifier`` in Distributed-mode

.. code-block:: bash

   $ valgrind --tool=memcheck --leak-check=yes --leak-resolution=high jubaclassifier -n test -z localhost:2181 -s 0 -i 0 -I 60 > valgrind.log 2>&1

3. Run ``xxxxx.py``

.. code-block:: bash

   $ ./xxxxx.py
