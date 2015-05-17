=====
AAIS  
=====

Intro
=====

A python based Auto Adjust Inventory for Suricata IDS/IPS/NSM. 
The idea is to be able to collect useful for the tuning of Suricata information at start up and document that in a yaml inventory file.



How to use
==========

Make sure you have python and python yaml installed.On Debian/Ubuntu like systems - ``apt-get install python python-yaml ethtool``.

To run the script: ::

 python aais.py

That will produce a ``SysInventory.yml`` yaml inventory file in the same directory.
