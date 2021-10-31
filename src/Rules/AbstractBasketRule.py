#!/usr/bin/env python
# coding: utf-8

# In[2]:

import sys

# print(sys.path)

from abc import ABC, abstractmethod
class AbstractBasketRule:
    @abstractmethod
    def isApplicable(self,basket):
        pass


# In[ ]:




