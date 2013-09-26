#!/bin/sh

#dionaea install script - run as ./dionaea-setup.sh "private key" "user@host"

SCRIPT="#install dionaea and p0f
sudo add-apt-repository ppa:honeynet/nightly
sudo apt-get update
sudo apt-get --yes --force-yes install dionaea sqlite p0f

#set up directories

sudo mkdir /var/p0f/
sudo mkdir -p /var/dionaea/wwwroot
sudo mkdir -p /var/dionaea/binaries
sudo mkdir -p /var/dionaea/log
sudo mkdir -p /var/dionaea/bistreams
sudo chown -R nobody:nogroup /var/dionaea/

#edit config

sudo mv /etc/dionaea/dionaea.conf.dist /etc/dionaea/dionaea.conf
sudo sed -i 's/var\/dionaea\///g' /etc/dionaea/dionaea.conf
sudo sed -i 's/log\//\/var\/dionaea\/log\//g' /etc/dionaea/dionaea.conf

#start the honeypot
sudo dionaea -c /etc/dionaea/dionaea.conf -w /var/dionaea -u nobody -g nogroup -D"

sudo ssh -o "StrictHostKeyChecking no" -i $1 $2 "${SCRIPT}"