#! bin/bash
echo " instalando paquetes de python"
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo apt-get install python-pip
sudo apt-get install python-picamera
sudo apt-get install python pyserial
sudo apt install python-smbus
pip install psutil
pip install commands
sudo pip install pi-ina219
#############################################
# video
echo " Instalando video"
cd /usr/src
sudo mkdir mjpg-streamer
sudo chown `whoami`:users mjpg-streamer
cd mjpg-streamer
git clone https://github.com/jacksonliam/mjpg-streamer.git .
sudo apt-get install libv4l-dev libjpeg8-dev imagemagick build-essential cmake subversion
cd mjpg-streamer-experimental

make
echo "video instalado "
############################################
# pymultiwii
echo "instalando pymultiwii"
git clone https://github.com/alduxvm/pyMultiWii.git
cd pyMultiWii
pip install .
echo "pymultiwwi instalado"



