#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[22]:


import json


# In[35]:


pd.read_json("https://api.github.com/repos/pandas-dev/pandas/issues")


# In[36]:


import requests
url="https://api.github.com/repos/pandas-dev/pandas/issues"


# In[37]:


data=requests.get(url)


# In[38]:


data


# In[39]:


data1=data.json()


# In[40]:


data1


# In[41]:


len(data1)


# In[42]:


data1[0]['user']['id']


# In[43]:


for i in range(len(data1)):
    print(data1[i]['user']['id'])


# In[44]:


data1


# In[45]:


data2=pd.DataFrame(data1, columns=['url','repositary-url','labels_url','user'])


# In[71]:


data3=data2['user']


# In[72]:


data3


# In[64]:


data3.to_csv('fata1.csv')


# In[65]:


ls


# In[61]:


fata2=pd.DataFrame(data1,columns=['url','repositary-url','labels_url','user',[pd.DataFrame(data3,columns=['login', 'id','node_id','avatar_url','gravatar_id','url','html_url','followers_url','following_url','gists_url','starred_url','subscriptions_url','organizations_url','organizations_url','repos_url','events_url','received_events_url','type','site_admin'])]])


# In[68]:


fata2.to_csv('cata1.csv')


# In[70]:


ls


# In[74]:


fata2


# In[59]:


data2


# In[75]:


len(fata2)


# In[ ]:




