
#Installs nepenthes, adds a random package mirror but hey its a honeypot.
#Pacific Northwest National Laboratory must be trust worthy...
sudo echo 'deb http://mirror.pnl.gov/ubuntu/ lucid main universe' >> /etc/apt/sources.list
sudo apt-get update
sudo apt-get install nepenthes

#to start run 'sudo nepenthes'