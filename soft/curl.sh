#!/bin/bash

C=curl-7.28.1
cd /x/soft
tar --lzma -xvf $C.tar.lzma
cd $C
./configure
make
make install
