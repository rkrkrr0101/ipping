#!/usr/bin/env python
# coding: utf-8

# In[44]:


import threading
import configparser
import time
import ping3


# In[45]:


def run(ip):
    #cmd='ping -n 1 -w 1 '+ip
    resp = ping3.ping(ip,timeout=1)
    if resp == None:
        res=1
    else:
        res=0 

    conf=configparser.ConfigParser()
    conf['abc']={}
    conf['abc'][ip]=str(res)
    with open(ip+'.ini','w',encoding='utf-8') as configfile:
        conf.write(configfile)


# In[46]:


readconf=configparser.ConfigParser()
readconf.read('config.ini',encoding='utf8')
iptable=readconf.sections()


# In[47]:


#iptable=['127.0.0.1','132.168.42.3','127.0.0.1','127.0.0.1','132.168.41.3']
while(True):
    for i in iptable:

        t= threading.Thread(target=run,args=(i,))
        t.start()
    time.sleep(1)
    


    


# In[29]:





# In[ ]:





# In[ ]:




