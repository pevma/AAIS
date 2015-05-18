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
import subprocess

class NIC:
  
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
  
  def getInterfaceStats(self):
    multi_interface_stats = {}
    
    intf_available = self.getInterfaces()
    
    for interface in intf_available:
      interface_stats_list = []
      interface_stats_list = subprocess.Popen(["ethtool", "-S", interface], stdout=subprocess.PIPE).communicate()[0].split("\n")
      
      # Delete the first line  - NIC statistics:
      del interface_stats_list[0]
      # Filter non present and empty values
      interface_stats_list = filter(None, interface_stats_list)
      
      # Create the dictionary
      interface_stats =  {k:v for k,v in (x.split(':') for x in interface_stats_list) }
      # strip spaces and tabs
      interface_stats =  dict(map(str.strip,x) for x in interface_stats.items())
      #for key, value in interface_stats.items(): print key, '>', value
      
      multi_interface_stats[interface] = interface_stats
      
    
    return multi_interface_stats
  
  def getInterfaceDriverInfo(self):
    multi_interface_driver_info = {}
    
    intf_available = self.getInterfaces()
    
    for interface in intf_available:
      interface_driver_info_list = []
      interface_driver_info_list = subprocess.Popen(["ethtool", "-i", interface], stdout=subprocess.PIPE).communicate()[0].split("\n")
      
      # Delete the first line  - NIC statistics:
      del interface_driver_info_list[0]
      # Filter non present and empty values
      interface_driver_info_list = filter(None, interface_driver_info_list)
      
      # Create the dictionary, splitting on the first occurrence of ":"
      interface_driver =  {k:v for k,v in (x.split(':',1) for x in interface_driver_info_list) }
      # strip spaces and tabs
      interface_driver =  dict(map(str.strip,x) for x in interface_driver.items())
      #for key, value in interface_driver.items(): print key, '>', value
      
      multi_interface_driver_info[interface] = interface_driver
      
    
    return multi_interface_driver_info








