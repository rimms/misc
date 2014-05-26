log4cxx sample
==============

Download and Insall log4cxx
---------------------------

::

  $ .install.sh


Build this sample
-----------------

::

  $ ./waf configure
  $ ./waf


Run
---

::

  $ ./build/logging-sample config/log4cxx.xml
  $ edit config/log4cxx.xml
  $ ./build/logging-sample config/log4cxx.xml
     :


Requirements
------------

* Jubatus 0.5.0 ora later (``jubatus::util::lang::noncopyable`` is used in this sample)
* automake
* libtool

