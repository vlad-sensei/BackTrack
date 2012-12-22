#!/usr/bin/env python3
import datetime, os.path

def makeloot(s):
  d='/x/loot/' + s + '_' + str(datetime.datetime.now()).split('.')[0].replace(' ','_') + '/'
  if not os.path.exists(d): os.makedirs(d)
  return d
