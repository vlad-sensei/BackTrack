#!/bin/bash

echo Check Internet Connection!
BTD='/root/Private/BackTrack'

# Read Password
#echo -n Password: 
#read -s password
#echo

passwd

#update
echo Updating..
apt-get update
apt-get dist-upgrade -y

echo Updating Metasploit..
msfupdate

#install private dir and make links

ecryptfs-setup-private
ecryptfs-mount-private

cd /root/Private/
git clone https://github.com/vlad-sensei/BackTrack.git
cd /root/

mv .bash_history /root/Private/.bash_history
ln -s /root/Private/.bash_history .bash_history
ln -s $BTD/rc/bashrc .bashrc

mv -r  /root/Desktop /root/Private/Desktop
ln -s $BTD/dt /root/Desktop

#add to bash.rc PATH and move bash.history to private dir

echo PATH=\$PATH: #add new path here
