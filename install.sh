#!/bin/bash

echo Check Internet Connection!

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

#install private dir  and make links


ecryptfs-setup-private
ecryptfs-mount-private

cd /root/Private/
git clone https://github.com/vlad-sensei/BackTrack.git
cd /root/



#add to bash.rc PATH and move bash.history to private dir

echo PATH=\$PATH: #add new path here
