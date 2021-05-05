#!/bin/bash

cp Bloody.flf /usr/share/figlet #Banner
apt-get update
apt-get install lolcat -y #Dependency
apt-get install figlet -y #Dependency
pip3 install dnspython
echo "DONE :)"
