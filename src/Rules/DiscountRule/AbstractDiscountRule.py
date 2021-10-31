#!/usr/bin/env python
# coding: utf-8

# In[4]:

import sys
import os
path_parent = os.path.realpath(r'../')
# print(path_parent)
sys.path.append(path_parent)

from AbstractBasketRule import AbstractBasketRule
from abc import ABC, abstractmethod
class AbstractDiscountRule(AbstractBasketRule):
    @abstractmethod
    def getDiscount(self,basket):
        pass


# In[ ]:




