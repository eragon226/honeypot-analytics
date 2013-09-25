#!/bin/sh

#install dionaea and p0f
sudo add-apt-repository ppa:honeynet/nightly
sudo apt-get update
sudo apt-get install dionaea sqlite p0f

#set up directories

sudo mkdir /var/p0f/
sudo mkdir -p /var/dionaea/wwwroot
sudo mkdir -p /var/dionaea/binaries
sudo mkdir -p /var/dionaea/log
sudo mkdir -p /var/dionaea/bistreams
sudo chown -R nobody:nogroup /var/dionaea/

#edit config

sudo rm /etc/dionaea/dionaea.conf.dist
sudo mv dionaea.conf /etc/dionaea/dionaea.conf
sudo dionaea -c /etc/dionaea/dionaea.conf -w /var/dionaea -u nobody -g nogroup -D

#install system services

sudo chmod +x /etc/init.d/p0f
sudo chmod +x /etc/init.d/dionaea

#start the honeypot
sudo /etc/init.d/p0f start
sudo /etc/init.d/dionaea start

