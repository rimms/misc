How to test
===========

LinearMixer (Use linear classifier)
-----------------------------------

1. Register config to Zookeeper

.. code-block:: bash

   $ jubaconfig -c write -f linear_config.json -z localhost:2181 -t classifier -n test

2. Start ``jubaclassifier`` in Distributed-mode

.. code-block:: bash

   $ jubaclassifier -n test -z localhost:2181 -p 9000
   $ jubaclassifier -n test -z localhost:2181 -p 9001

3. Run ``train.py`` and ``do_mix.py``

.. code-block:: bash

   $ python train.py -p 9000
   $ python train.py -p 9000
   $ python do_mix.py -p 9000
   $ python do_mix.py -p 9001

