
1. Register config to Zookeeper

.. code-block:: bash

   $ jubaconfig -c write -f config.json -z localhost:2181 -t recommender -n test

2. Start ``jubarecommender`` in Distributed-mode (**Server-2**)

.. code-block:: bash

   $ jubarecommender -p 9002 -n test -x broadcast_mixer -t 0 -I 6000 -s 0 -i 1 -z localhost:2181

3. Start ``jubarecommender`` in Distributed-mode (**Server-3**)

.. code-block:: bash

   $ jubarecommender -p 9003 -n test -x broadcast_mixer -t 0 -I 6000 -s 0 -i 1 -z localhost:2181

4. Start ``jubarecommender`` in Distributed-mode w/ break-point via gdb (**Server-1**)

.. code-block:: bash

   $ gdb -x bp-in-pull.gdb --args jubarecommender -p 9001 -n test -x broadcast_mixer -t 0 -I 6000 -s 0 -i 1 -z localhost:2181
   (gdb) run
   (gdb) c    ... (Skip pull at start)
   (gdb) c    ... (Skip pull at start)

5. ``update_row`` to Server-2

.. code-block:: bash

   $ ./update_row.py -i "ID1" -p 9002

  * Server-1: Stopped in break-Point

6. Delete break-point in Server-1

.. code-block:: bash

   (gdb) clear

7. ``get_all_rows`` to Server-1, 2, 3

.. code-block:: bash

   $ ./get_all_rows.py -p 9001 9002 9003

  * Server-1: []
  * Server-2: ["ID1"]
  * Server-3: []

8. ``update_row`` to Server-3

.. code-block:: bash

   $ ./update_row.py -i "ID2" -p 9003

9. ``get_all_rows`` to Server-1, 2, 3

.. code-block:: bash

   $ ./get_all_rows.py -p 9001 9002 9003

  * Server-1: ["ID2"]
  * Server-2: ["ID1", "ID2"]
  * Server-3: ["ID2", "ID1"]

10. Release break-point in Server-1

.. code-block:: bash

   (gdb) c -a

11. ``get_all_rows`` to Server-1, 2, 3

.. code-block:: bash

   $ ./get_all_rows.py -p 9001 9002 9003

  * Server-1: ["ID2", "ID1"] is expected, but actual is ["ID2"]
  * Server-2: ["ID1", "ID2"]
  * Server-3: ["ID2", "ID1"]
