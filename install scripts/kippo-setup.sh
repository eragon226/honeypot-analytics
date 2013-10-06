#!/bin/sh

#kippo install script - run as ./kippo-setup.sh "private key" "user@host"

SCRIPT="sudo apt-get update
sudo apt-get --yes --force-yes upgrade
sudo sed -i -e 's/Port 22/Port 1234/g' /etc/ssh/sshd_config
sudo reload ssh
sudo apt-get --yes --force-yes install python-dev openssl python-openssl python-pyasn1 python-twisted subversion authbind
sudo useradd -d /home/kippo -s /bin/bash -m kippo -g sudo
sudo touch /etc/authbind/byport/22
sudo chown kippo /etc/authbind/byport/22
sudo chmod 777 /etc/authbind/byport/22
su kippo
cd
svn checkout http://kippo.googlecode.com/svn/trunk/ ./kippo 
cd kippo
sed -i -e 's/ssh_port = 2222/ssh_port = 22/g' kippo.cfg.dist
sed -i -e 's/twistd -y /authbind --deep twistd -y /g' start.sh
mv kippo.cfg.dist kippo.cfg
"
#To start the honeypot run ./start.sh

sudo ssh -v -o "StrictHostKeyChecking no" -i $1 $2 "${SCRIPT}"