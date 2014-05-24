#!/bin/bash

LOG4CXX_HOME=$HOME/local/log4cxx

mkdir downloads
pushd downloads

# APR
wget http://ftp.riken.jp/net/apache//apr/apr-1.5.1.tar.gz
tar xvfz apr-1.5.1.tar.gz
pushd apr-1.5.1
./configure --prefix=$LOG4CXX_HOME
make
make install
popd

# APR Util
wget http://ftp.tsukuba.wide.ad.jp/software/apache//apr/apr-util-1.5.3.tar.gz
tar xvfz apr-util-1.5.3.tar.gz
pushd apr-util-1.5.3
./configure --prefix=$LOG4CXX_HOME --with-apr=$LOG4CXX_HOME
make
make install
popd

# log4cxx
wget http://ftp.riken.jp/net/apache/logging/log4cxx/0.10.0/apache-log4cxx-0.10.0.tar.gz
tar xvfz apache-log4cxx-0.10.0.tar.gz
pushd apache-log4cxx-0.10.0
sed -i '18i#include <string.h>' src/main/cpp/inputstreamreader.cpp
sed -i '18i#include <string.h>' src/main/cpp/socketoutputstream.cpp
sed -i '19i#include <string.h>' src/examples/cpp/console.cpp
sed -i '20i#include <stdio.h>' src/examples/cpp/console.cpp
./configure --prefix=$LOG4CXX_HOME --with-apr=$LOG4CXX_HOME --with-apr-util=$LOG4CXX_HOME
make
make install

export CPLUS_INCLUDE_PATH=$LOG4CXX_HOME/include:$CPLUS_INCLUDE_PATH
export LD_LIBRARY_PATH=$LOG4CXX_HOME/lib:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=$LOG4CXX_HOME/lib/pkgconfig:$PKG_CONFIG_PATH
