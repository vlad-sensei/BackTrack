#!/usr/bin/env python

import subprocessi, os.path

x=subprocess.Popen

l={}
B='/root/Private/BackTrack'
l['/root/Private/.bash_history']='/root/.bash_history'
l[B+'/rc/bashrc']='/root/.bashrc'
l[B]='/x'
l[B+'update.sh']='/x/sc/bt-update'
l['/x/sc']='/x/dt/Scripts'
l['/x/rc']='/x/dt/Conf'

for key in l:
  if not os.path.exists(l[key]): x(['ln', '-s', key, l[key]])

exit 0