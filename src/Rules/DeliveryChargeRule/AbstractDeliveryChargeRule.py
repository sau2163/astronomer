#!/usr/bin/env python
# coding: utf-8

# In[4]:
import sys
import os
# print(os.getcwd())
path_parent = os.path.dirname(os.getcwd())

sys.path.append(path_parent)

from AbstractBasketRule import AbstractBasketRule
from abc import ABC, abstractmethod
class AbstractDeliveryChargeRule(AbstractBasketRule):
    @abstractmethod
    def getDeliveryCharge(self,basket):
        pass


# In[ ]:




