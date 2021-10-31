#!/usr/bin/env python
# coding: utf-8

# In[4]:
import sys
import os
path_parent = os.path.realpath(r'../../Entity')
# print(path_parent)
sys.path.append(path_parent)
from LineItem import LineItem
from AbstractDiscountRule import AbstractDiscountRule

class SecondHalfPriceDiscountRule(AbstractDiscountRule):
    
    def __init__(self, product):
        self.product = product
        
    def isApplicable(self, basket):
        for item in basket.getBasketItems():
            if(not isinstance(item, LineItem)):
                continue
            if( (item.getProduct().getCode()==self.product.getCode()) and (item.getQuantity()>=2) ):
                return True
        return False
        
    def getDiscount(self, basket):
        discountedProductItem = None
        for item in basket.getBasketItems():
            if(not isinstance(item, LineItem)):
                continue
            if( (item.getProduct().getCode()==self.product.getCode()) and (item.getQuantity()>=2) ):
                return Price(
                    (item.getQuantity/2) * (item.getProduct().getPrice()/2),
                    item.getProduct().getPrice().getCurrency()
                )
                break;
        
        return None


# In[ ]:




