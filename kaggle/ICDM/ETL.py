
# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')


# In[2]:

ls data/


# In[3]:

import pandas as pd
from itertools import groupby, count
_figsize = (13.5,8)


# In[4]:

cookie_all_basic = pd.read_csv('data/cookie_all_basic.csv')
dev_train_basic = pd.read_csv('data/dev_train_basic.csv')
dev_test_basic = pd.read_csv('data/dev_test_basic.csv')
ipagg_all = pd.read_csv('data/ipagg_all.csv')
sampleSubmission = pd.read_csv('data/sampleSubmission.csv')
#  = pd.read_csv('')


# In[5]:

property_category = pd.read_csv('data/property_category.csv')
id_all_ip = pd.read_csv('data/id_all_ip.csv')
id_all_property = pd.read_csv('data/id_all_property.csv')


# In[6]:

dev_all = pd.concat([dev_test_basic, dev_train_basic], ignore_index=True)
print dev_test_basic.shape[0], dev_train_basic.shape[0], dev_all.shape[0]


# In[7]:

# print "unique devices: \n%s " % ('\n'.join(["%d. %s" % (i, j) for i, j in enumerate(dev_all.device_type.unique())]))
# print "\nunique dev types: \n%s " % (["%d. %s" % (i, j) for i, j in enumerate(dev_all.device_os.unique())])
uniq_dev_types = dev_all.device_type.unique()
uniq_dev_os = dev_all.device_os.unique()
uniq_country = dev_all.country.unique()
uniq_drawbridge_handle_train =  dev_all.drawbridge_handle.unique()
print "unique device types: %s " % (len(np.delete(uniq_dev_types, np.where(uniq_dev_types == '-1'))))
print "unique device OS types: %s " % (len(np.delete(uniq_dev_os, np.where(uniq_dev_os == '-1'))))
print "unique device countries: %s " % (len(np.delete(uniq_country, np.where(uniq_country == '-1'))))
print "unique train drawbridge handles: %s " % (len(np.delete(uniq_drawbridge_handle_train, np.where(uniq_drawbridge_handle_train == -1))))


# In[8]:

# def as_range(iterable):
#     l = list(iterable)
#     if len(l) > 1:
#         return (l[0], l[-1])
#     else:
#         return l[0]
    
# [as_range(g) for _, g in groupby(dev_all.drawbridge_handle, key=lambda n, c=count(): n-next(c))]

s = dev_all.groupby("device_type").agg(lambda x:len(x.unique()))
# s
s = s.drop(s.index[0]).reset_index()
ax = s.plot(x='device_type', y='device_id', 
            lw=2, title='device_type distribution', 
            figsize = _figsize, kind='bar')
ax.set_ylabel("device_id count")


# In[14]:

# "anonymous_c1_1307" in dev_train_basic.anonymous_c1
dev_all


# In[15]:

ipagg_all


# In[9]:

cookie_all_basic


# In[11]:

property_category


# In[12]:

id_all_property


# In[13]:

id_all_ip

