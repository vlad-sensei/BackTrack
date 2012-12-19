#!/bin/bash

cd /x/soft
git clone https://github.com/Ettercap/ettercap.git
cd ettercap
mkdir build
cd build
cmake ../
make
make install

