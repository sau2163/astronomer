#!/usr/bin/env python
# coding: utf-8

# In[4]:
import sys
import os


from AbstractDeliveryChargeRule import AbstractDeliveryChargeRule

class OrderValueBasedDeliveryChargeRule(AbstractDeliveryChargeRule):
    
    def __init__(self, minOrderValue, maxOrderValue, deliveryCharge):
        if((minOrderValue is None ) and (maxOrderValue is None)):
               raise ValueError('Invalid Delivery Charge -  both cannot be null')
           
        self.minOrderValue = minOrderValue
        self.maxOrderValue = maxOrderValue
        self.deliveryCharge = deliveryCharge
        
    def isApplicable(self, basket):
        orderValue = basket.calculateOrderValueTotal() - basket.calculateDiscount()
        
        if((maxOrderValue is None ) and self.maxOrderValue>= orderValue):
            return True
        
        if((maxOrderValue is None ) and self.minOrderValue< orderValue):
            return True
        
        return ( (orderValue > self.minOrderValue) and (orderValue <= self.maxOrderValue) )
    
    def getDeliveryCharge(self, basket):
        return self.deliveryCharge
        
        


# In[ ]:




