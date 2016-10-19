
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[3]:

import quandl


# In[4]:

quandl.ApiConfig.api_key = "x6yqoXJqQriyqVRZf1LC"


# In[5]:

companies = pd.read_csv("bse_company_code.txt", sep="|", encoding = "ISO-8859-1")


# In[6]:

companies.head()


# In[7]:

#indexed_company = companies.set_index(['CODE'])


# In[8]:

#check_name = indexed_company.loc["BOM512161"]["STOCK"]


# In[9]:

#check_name


# In[10]:

company_codes = list(companies['CODE'])


# In[11]:

correct_code = []
for company_code in company_codes:
    code=str("BSE/") + str(company_code)
    correct_code.append(code)


# ## Get Data from quandl

# In[12]:

for code in correct_code:
    data = quandl.get(code)
    data.to_csv("./datasets/"+ str(company_codes[correct_code.index(code)]+".csv"))
    del data


# In[34]:

#mydata.to_csv("./datasets/"+ str(company_codes[10]+".csv"))


# In[ ]:



