#!/bin/bash
sudo -H pip install virtualenv
virtualenv -p /usr/bin/python2.7 async-kart
source venv/bin/activate
cd gym-mupen64plus/
sudo -H pip install -e .
cd ..
sudo -H pip install gym
cp input-driver/mupen64plus-input-bot.so /usr/local/lib/mupen64plus/mupen64plus-input-bot.so 
sudo apt-get install python-pip
sudo apt-get install xvfb xserver-xephyr vnc4server
sudo pip install pyvirtualdisplay
sudo dpkg -i virtualgl_2.2.2_amd64.deb 
cp ROM/marioKart.n64 gym-mupen64plus/gym-mupen64plus/ROMs/marioKart.n64

