#!/usr/bin/python
# -*- coding: utf-8 -*-

##                                       ##
# Author: Peter Manev                     #
# peter.manev@openinfosecfoundation.org   #
##                                       ##

# you need to 
# apt-get install python-yaml
# sudo yum install PyYAML (on CentOS/Fedora/RedHat)

import platform



class harvestOS:
  
  # Important - by default python-yaml returns "True" or "Flase"
  # for any options set to "yes" or "no" and NOT the "yes" or "no" themselves
  
  def getOSArch(self):
    
    self.osArch = platform.architecture()
    return self.osArch
    
  
  
  def getOSUname(self):
    # Returns a tuple of strings 
    # (system, node, release, version, machine, processor)
    self.osUname = platform.uname()
    return self.osUname
    
  
  
  def getOSLinux_distribution(self):
    # Returns a tuple (distname,version,id) 
    self.osUname = platform.linux_distribution()
    return self.osUname
  
  
