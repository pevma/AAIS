#!/usr/bin/python
# -*- coding: utf-8 -*-

##                                       ##
# Author: Peter Manev                     #
# peter.manev@openinfosecfoundation.org   #
##                                       ##


import os
import re
import sys
import time
import glob

class harvestNIC:
  
  def getInterrupts(self):
    f_interrupts = open("/proc/interrupts", "r")
    f_interrupts.seek(0)
    ts = int(time.time())
    
    # Get number of CPUs from description line.
    num_cpus = len(f_interrupts.readline().split())
    intf_interrupts = {}
    #print num_cpus
    
    intf_available = self.getInterfaces()
    #print "INTERFACES AVAILABLE", intf_available
    
    for interface in intf_available:
      interrupts_num =  0
      
      for line in f_interrupts:
        cols = line.split()
        irq_type = cols[0].rstrip(":")
        #print irq_type
        if irq_type.isalnum():
	  if irq_type.isdigit():
	    if cols[-2] == "PCI-MSI-edge" and interface and "TxRx" in cols[-1]:
	      irq_type = cols[-1]
	      #print irq_type
	      interrupts_num += 1
	      
      intf_interrupts[interface] = interrupts_num
    
    f_interrupts.close()
    
    #print "Interface > interrupts"
    #for intf, interrupts in intf_interrupts.items(): print intf, '>', interrupts
    
    return intf_interrupts
    
  
  
  def getInterfaces(self):
    net_dev = open("/proc/net/dev", "r")
    dev = net_dev.readlines()
    net_dev.close()
    
    net_interfaces = []
    #print "dev count", len(dev)
    
    for line in dev[2:]: 
      #the thrid line onwards should contain the interfaces
      intf = line[:line.index(":")].strip()
      net_interfaces.append(intf)
      
    
    #remove loopback interface
    net_interfaces.remove("lo")
    
    #print "net_interfaces ->", net_interfaces
    return net_interfaces

