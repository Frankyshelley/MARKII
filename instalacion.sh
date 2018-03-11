#! bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo apt-get install python-pip
sudo apt-get install python-picamera
sudo apt-get install python pyserial
sudo apt install python-smbus
pip3 install psutil
pip3 install commands
sudo pip3 install pi-ina219


git clone https://github.com/metachris/RPIO.git --branch v2 --single-branch
cd RPIO
sudo python setup.py install


