#!/usr/bin/env python

import subprocess, os.path

x=subprocess.Popen

d=[]
d.append('/x/loot')

x(['ln', '-s', '/x/loot', '/x/dt/Loot'])

l={}
B='/root/Private/BackTrack'
l['/root/Private/.bash_history']='/root/.bash_history'
l[B+'/rc/bashrc']='/root/.bashrc'
#l[B]='/x'
l[B+'/update.sh']='/x/sc/bt-update'
l['/x/sc']='/x/dt/Scripts'
l['/x/rc']='/x/dt/Conf'
l['/x/sc/gsh']='/x/dt/Gnome-Shell'
l['/x/loot']='x/dt/Loot'

for dr in d:
  if not os.path.exists(dr): os.makedirs(dr)

for key in l:
  if not os.path.exists(l[key]): x(['ln', '-s', key, l[key]])

if not os.path.exists('/etc/init.d/chmac'):
  x(['cp', '/x/sc/chmac', '/etc/init.d/chmac'])
  x(['update-rc.d', 'chmac', 'defaults'])

exit(0)
