#!/usr/bin/python
# -*- coding: utf-8 -*-

##                                       ##
# Author: Peter Manev                     #
# peter.manev@openinfosecfoundation.org   #
##                                       ##

# you need to 
# apt-get install python-yaml
# sudo yum install PyYAML (on CentOS/Fedora/RedHat)

import yaml
import Harvest


if __name__ == "__main__":
  
  inventory = {}
  inventory["OS"] = {}
  
  osArch = Harvest.OS().getOSArch()
  inventory["OS"]["Architecture"] = osArch[0]
  inventory["OS"]["Linkage"] = osArch[1]
  
  # system, node, release, version, machine, processor
  osUname = Harvest.OS().getOSUname()
  inventory["OS"]["System"] = osUname[0]
  inventory["OS"]["Node"] = osUname[1]
  inventory["OS"]["Release"] = osUname[2]
  inventory["OS"]["Kernel"] = osUname[2].split('-')[0]
  #inventory["OS"]["Version"] = osUname[3]
  inventory["OS"]["Machine"] = osUname[4]
  inventory["OS"]["Processor"] = osUname[5]
  
  # distname,version,id
  osLinux_dist = Harvest.OS().getOSLinux_distribution()
  inventory["OS"]["Distname"] = osLinux_dist[0]
  inventory["OS"]["Version"] = osLinux_dist[1]
  inventory["OS"]["Id"] = osLinux_dist[2]
  
  inventory["CPU"] = {}
  # model, frequency, num_cpu
  systemCpu = Harvest.CPU().getCPU()
  # note strip() is used below in order for the yaml.dump
  # to not put ' ' around the string
  inventory["CPU"]["Model"] = systemCpu[0].split('@')[0].strip()
  inventory["CPU"]["Frequency"] = systemCpu[1]
  inventory["CPU"]["Count"] = systemCpu[2]
  
  inventory["Memory"] = {}
  # a dict of /proc/meminfo
  systemMemory = Harvest.Memory().getMemory()
  #print systemMemory
  inventory["Memory"] = systemMemory 
  
  inventory["Interface_Interrupts"] = {}
  # a combined effort from HarvestNIC** functions
  # returns Interface : Interrupts dictionary
  interfacesInterrupts = Harvest.NIC().getInterrupts()
  inventory["Interface_Interrupts"] = interfacesInterrupts
   
  
  with open('SysInventory.yml', 'w') as yaml_file:
    yaml_file.write( yaml.dump(inventory, default_flow_style=False))
    

