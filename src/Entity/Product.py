#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Product:
    def __init__(self,code, name, colour, price):
        self.code=code
        self.name=name
        self.colour=colour
        self.price=price
        
    def getCode(self):
        return self.code
    def setCode(self, code):
        self.code = code
        
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
        
    def getColour(self):
        return self.colour
    def setColour(self, colour):
        self.colour = colour
        
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price


# In[ ]:




