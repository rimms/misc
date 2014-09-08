The codes that can reproduce jubatus#717
----------------------------------------

* ``new_client``

  Create new client for each connection.
  This code will reproduce jubatus#717 situation.

* ``one_client``

  Use one client for each connection.
  This code will **not** reproduce jubatus#717 situation.


How to Build
~~~~~~~~~~~~

.. code-block:: bash

   $ make
