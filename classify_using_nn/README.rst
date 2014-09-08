Classify Shogun using Nearest Neighbour
---------------------------------------

1. Run jubanearest_neighbour

   ```
   $ jubanearest_neighbor -f bin.json &
   ```

2. Run test script

   ```
   $ ./shogun_using_nn.py
   足利 慶喜  ...  足利=8.57890176773 北条=5.32667899132 徳川=3.11914455891
   足利 義昭  ...  足利=12.1789979935 徳川=1.57138991356
   北条 守時  ...  北条=12.5856430531
   ```

Requirements
~~~~~~~~~~~~

* Jubatus 0.6.2 or later
* Jubatus Python Client 0.6.0 or later
* Python 2.7.x


Note
~~~~

jubanearest_neighbor with ``idf.json`` does not work correctly. See https://github.com/jubatus/jubatus/issues/869 .
