#!/usr/bin/env python
# coding: utf-8

# # 1
# 

# In[1]:


import numpy as np
x=np.zeros(10)
x[4]=1
x


# # 2

# In[3]:


import numpy as np
vector=np.arange(10,49)
print("original vector:")
print(vector)


# # 3

# In[4]:


import numpy as np
x=np.arange(0,9).reshape(3,3)
print(x)


# # 4

# In[5]:


q=np.array([1,2,0,0,4,0])
q[q>0]


# # 5

# In[7]:


z=np.random.randint(1,100,(10,10))
print(z)
zmin,zmax=z.min(),z.max()
print('minimum value is:',zmin)
print('maximum value is:',zmax)


# # 6

# In[8]:


import numpy as np
vector=np.random.random(30)
print("original array:")
print(vector)
print('mean value is:',np.mean(vector))


# In[ ]:




