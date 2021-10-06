#!/usr/bin/env python
# coding: utf-8

# In[20]:


import threading
import subprocess
import configparser
import time


# In[21]:


def run(ip):
    cmd='ping -n 1 -w 1 '+ip
    res=subprocess.call(cmd)
    
    conf=configparser.ConfigParser()
    conf['abc']={}
    conf['abc'][ip]=str(res)
    with open(ip+'.ini','w',encoding='utf-8') as configfile:
        conf.write(configfile)


# In[24]:


readconf=configparser.ConfigParser()
readconf.read('config.ini',encoding='utf8')
iptable=readconf.sections()


# In[25]:


#iptable=['127.0.0.1','132.168.42.3','127.0.0.1','127.0.0.1','132.168.41.3']
while(True):
    for i in iptable:

        t= threading.Thread(target=run,args=(i,))
        t.start()
    time.sleep(1)
    

print("main thread end")
    


# In[19]:





# In[ ]:




