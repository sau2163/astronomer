#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Currency:
    def __init__(self,code, name , symbol):
        self.code = code
        self.name = name
        self.symbol = symbol
        
    def getCode(self):
        return self.code
    def setCode(self,code):
        self.code = code
    
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
        
    def getSymbol(self):
        return self.symbol
    def setSymbol(self,symbol):
        self.symbol = symbol


# In[3]:






