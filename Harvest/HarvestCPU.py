#!/usr/bin/python
# -*- coding: utf-8 -*-

##                                       ##
# Author: Peter Manev                     #
# peter.manev@openinfosecfoundation.org   #
##                                       ##



class harvestCPU:
  
  # Important - by default python-yaml returns "True" or "Flase"
  # for any options set to "yes" or "no" and NOT the "yes" or "no" themselves
  
  def getCPU(self):
    with open('/proc/cpuinfo', 'r') as cpuinfo:
      cpu = []
      for line in cpuinfo:
        # Ignore the blank line separating the information between
        # details about two processing units
        if line.strip():
            if line.rstrip('\n').startswith('model name'):
                cpu.append(line.rstrip('\n').split(':')[1])
                
    # returns, example:
    # model , frequency, num_cpu
    cpuinfo.close()
    return ( cpu[0], cpu[0].split()[-1], len(cpu) )
  
  
  
