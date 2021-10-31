#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Price:
    def __init__(self, price, currency):
        self.price=price
        self.currency = currency
    
    def getPrice(self):
        return self.price
    
    def getCurrency(self):
        return self.currency

