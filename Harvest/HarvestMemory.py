#!/usr/bin/python
# -*- coding: utf-8 -*-

##                                       ##
# Author: Peter Manev                     #
# peter.manev@openinfosecfoundation.org   #
##                                       ##

import re

class harvestMemory:
  
  # Important - by default python-yaml returns "True" or "Flase"
  # for any options set to "yes" or "no" and NOT the "yes" or "no" themselves
  
  def getMemory(self):
    
    # dict of data from meminfo str - int
    # Values are in KB.
    
    #re_parser = re.compile(r'^(?P<key>\S*):\s*(?P<value>\d*)\s*kB')
    re_parser = re.compile(r'^(?P<key>\S*):\s*(?P<value>\d*)\s*')
    memory_info = {} # dictionary
    with open('/proc/meminfo', 'r') as meminfo:
      for line in meminfo:
        match = re_parser.match(line)
        if not match:
            continue # skip lines that don't parse
        key, value = match.groups(['key', 'value'])
        memory_info[key] = int(value)
    meminfo.close()
    return memory_info
  
  
  
