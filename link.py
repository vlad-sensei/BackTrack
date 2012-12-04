#!/usr/bin/env python

import subprocess, os.path

x=subprocess.Popen

l={}
B='/root/Private/BackTrack'
l['/root/Private/.bash_history']='/root/.bash_history'
l[B+'/rc/bashrc']='/root/.bashrc'
l[B]='/x'
l[B+'update.sh']='/x/sc/bt-update'
l['/x/sc']='/x/dt/Scripts'
l['/x/rc']='/x/dt/Conf'
l['/x/sc/gsh']='/x/dt/Gnome-Shell'

for key in l:
  if not os.path.exists(l[key]): x(['ln', '-s', key, l[key]])

if not os.path.existsfunc_closure.EX_CANTCREAT

exit(0)
