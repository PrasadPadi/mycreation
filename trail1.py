#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
x=np.arange(9).reshape(3,3)
y=np.arange(9,18).reshape(3,3)
print(x,y)


# In[14]:


import pandas as pd
ax=pd.DataFrame(x,columns=['a','b','c'],index=['d','e','f'])
bx=pd.DataFrame(y,columns=['a','b','c'],index=['d','e','f'])
print(ax) 
print(bx)


# In[18]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.catplot('a','b',data=ax,hue='c')


# In[19]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.catplot('a','b',data=bx,hue='c')


# In[ ]:




