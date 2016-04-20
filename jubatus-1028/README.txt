ZooKeeper:

  zkServer.sh start
  jubaconfig -n test -z localhost:2181 -c write -t classifier -f test.json

Server1:

  gdb -x bp-do_mix.gdb --args jubaclassifier -n test -p 9000 -z localhost:2181 -s 0 -i 0 -Z 120 -I 120 -c 4 -g log4cxx.xml
  (gdb) run

Server2:

  jubaclassifier -n test -p 9001 -z localhost:2181 -s 0 -i 0 -Z 120 -I 120 -c 4 -g log4cxx.xml

do_mix to Server1:

  ./do_mix.py
    => Breaks on Break Point

do_mix to Server2:

  ./do_mix.py
    => Breaks on Trining to get Master-Lock

Continue Server1:

  (gdb) c -a


Expected:

  do_mix-1.sh will finish
  do_mix-2.sh will finish
