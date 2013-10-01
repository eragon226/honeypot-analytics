honeypot-analytics
==================

There is no stable branch at the moment as there's no real functionality.  
Use case 1 should be fully done by 7/10 and a 0.1 bracnh will be created then.  

Putting data from honeynets to work - the plan is too create a platform which will allow for 
gathering as much data as possible from both captured malicious binaries and attack logs.

###Honeypots:

Initial plans are too work with nepenthes, dionaea and Kippo.

###Use Cases:

1 -
Setup honeypots on AWS with some tweaks from default settings, basic bash scipts should do it.  
Aggregate binaries and logs in one place, should be doable with a simple python server.  
Begin collecting data in to databases.   
  
2 -
Gathering more data from honeypots using p0f.  
Gathering more data from captured binaries using sandboxes and services like Virus Total.    
  
3-  
Look into analysing traffic logs - using tools like snort to look at exploits used and information like geo-location.  
Begin to take the information gathered and do some analysis on it as a whole and create some shiney d3.js pages - mapping origins of attacks,  graphing trends and looking into malware geneology.
  
###Plus's:  
  
Make it easy to install and setup honeypots properly - possibly fork setup scripts once they begin to become too  
project specific, leaving a barebones script for people who just want to set one up and leave it.  
  
Shiny graphs.  
  
Should give a lot of sample code of discrete operations - a lot of which are potentially useful on there own.

This is mostly just for me too learn stuff.  
  
###Technology:  
  
Bash, Python, Sqlite and d3.js at the moment.  
  
###Contact:  
  
@sam_bwut on twitter.  
  
