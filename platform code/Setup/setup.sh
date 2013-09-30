#!/bin/sh

#install dependencies needed for processor node
sudo apt-get install python sqlite git
git clone git://github.com/smarnach/pyexiftool.git
cd pyexiftool
sudo python setup.py install