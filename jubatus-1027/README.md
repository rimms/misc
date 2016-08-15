## How to Test

## Conditions

- Build jubatus_core and jubatus with ``-O0``.

## Scenario

1. Start ZooKeeper and register config

  ```sh
  $ zkServer.sh start
  $ jubaconfig -n test -z localhost:2181 -c write -t classifier -f test.json
  ```

2. Start ``jubaclassfier`` using gdb

  ```sh
  $ gdb -x bp.gdb --args jubaclassifier -n test -p 9000 -z localhost:2181 -Z 120
  (gdb) run
  ```

    => Breaks on Break-Point

3. Stop ZooKeeper

  ```sh
  $ zkServer.sh stop
  ```

4. Re-Start ``jubaclassifier`` and wait a little

  ```sh
  (gdb) c -a
  ```

## Expected

``jubaclassifier`` will stop with ERROR message.
