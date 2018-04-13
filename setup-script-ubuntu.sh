#!/bin/bash
sudo apt-get install tensorflow
sudo apt-get install python-pip
cd gym-mupen64plus/
sudo -H pip install -e .
cd ..
sudo -H pip install gym
sudo mkdir /usr/local/lib/mupen64plus
sudo cp input-driver/mupen64plus-input-bot.so /usr/local/lib/mupen64plus/
sudo apt-get install python-pip
sudo apt-get install xvfb xserver-xephyr vnc4server
sudo pip install pyvirtualdisplay
sudo dpkg -i graphic_driver/virtualgl_2.5.2_amd64.deb 
sudo cp ROM/marioKart.n64 gym-mupen64plus/gym_mupen64plus/ROMs/
sudo apt-get install mupen64plus
export PATH="/usr/games/:$PATH"
