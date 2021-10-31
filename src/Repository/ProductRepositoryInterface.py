#!/usr/bin/env python
# coding: utf-8

from abc import ABC, abstractmethod
class ProductRepositoryInterface(ABC):
    @abstractmethod
    def addProduct(self, product):
        pass
    
    @abstractmethod
    def findAll(self):
        pass
    
    @abstractmethod
    def findOneByCode(code):
        pass

