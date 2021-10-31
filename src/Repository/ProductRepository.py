#!/usr/bin/env python
# coding: utf-8

# In[4]:
import sys
import os
path_parent = os.path.realpath(r'../../Entity')
# print(path_parent)
sys.path.append(path_parent)
from Product import Product
from ProductRepositoryInterface import ProductRepositoryInterface

class ProductRepository(ProductRepositoryInterface):
    
    products=[]
    
    def addProduct(self,product):
        self.products.append(product)
        
    def findOneByCode(self,code):
        for product in products:
            
            if(not isinstance(product,Product)):
                continue
            
            if(product.getCode()==code):
                return product
            
        return None
        
    
    def findAll(self):
        return self.products
