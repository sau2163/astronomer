#!/usr/bin/env python
# coding: utf-8

# In[1]:


class LineItem:
    def __init__(self,product, quantity=1):
        self.product = product
        self.quantity = quantity
    
    def getProduct(self):
        return self.product
    
    def getQuantity(self):
        return self.quantity
    def setQuantity(self, quantity):
        self.quantity = quantity
        
    def incrementQuantity(self,step=1):
        self.quantity +=step


# In[2]:



