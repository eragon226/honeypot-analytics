#!/bin/sh

#nepenthes install script - run as ./nepenthes-setup.sh "private key" "user@host"

SCRIPT="#Installs nepenthes, downloads it from a random mirror but hey its a honeypot anyway...
sudo apt-get install gdebi-core
wget http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/pool/universe/n/nepenthes/nepenthes_0.1.7-1_i386.deb
sudo gdebi nepenthes_0.1.7-1_i386.deb
#start the honeypot
sudo nepenthes"

sudo ssh -v -o "StrictHostKeyChecking no" -i $1 $2 "${SCRIPT}"