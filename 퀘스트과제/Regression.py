
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


# In[16]:


url='C:\\temp\\reg_quest.csv'
data=pd.read_csv(url)
print(data.head())


# In[13]:


results1 = smf.ols('symtot ~ re1 +self1', data=data).fit()
results2 = smf.ols('symtot ~ self1+self4+re6', data=data).fit()
results3 = smf.ols('symtot ~ age+re1+re2',data=data).fit()
resluts4 = smf.ols('symtot ~ re1+re2+re3+re4+age',data=data).fit()
results5 = smf.ols('symtot ~ self4+re4',data=data).fit()


# In[14]:


print(results1.summary())
print(results2.summary())
print(results3.summary())
print(results4.summary())
print(results5.summary())

