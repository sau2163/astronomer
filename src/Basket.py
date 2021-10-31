import sys
import os
path_parent_1 = os.path.realpath(r'./Entity')
path_parent_2 = os.path.realpath(r'./Rules/DiscountRule')
path_parent_3 = os.path.realpath(r'./Rules/DeliveryChargeRule')
path_parent_4 = os.path.realpath(r'./Repository')
path_parent_5 = os.path.realpath(r'./Rules')
# print(path_parent)
sys.path.append(path_parent_1)
sys.path.append(path_parent_2)
sys.path.append(path_parent_3)
sys.path.append(path_parent_4)
sys.path.append(path_parent_5)

from LineItem import LineItem
from AbstractDiscountRule import AbstractDiscountRule
from AbstractDeliveryChargeRule import AbstractDeliveryChargeRule
from ProductRepository import ProductRepository
from ProductRepositoryInterface import ProductRepositoryInterface


class Basket:
    discountRules=[]
    deliveryChargeRules=[]
    items=[]
    
    productsRepository=None
    
    def __init__(self):
        self.productsRepository = ProductRepository()
        
    def addProduct(self, code):
        product = self.productsRepository.findOneByCode(code)
        if(product is None):
            raise Exception(f"Product with code {0} is not valid and could not be added".format(code))
            
        key=-1
        for item in items:
            key=key+1
            if(item.getProduct().getCode()==product.getCode()):
                item.incrementQuantity()
                self.items[key]=item
                return True
            
        self.items = LineItem(product)
        
        return True
    
    def calculateOrderValueTotal(self):
        total=0.0
        for item in self.items:
            if(not isinstance(item,LineItem)):
                continue
            total = (item.getProduct().getPrice()) * item.getQuantity()
            
        return total
    
    def getGrandTotal(self):
        return self.calculateOrderValueTotal() + self.calculateDeliveryCosts() - self.calculateDiscount()
    
    
    def getBasketItems(self):
        return self.items
    
    def addDiscountRule(self,discountRule):
        self.discountRules.append(discountRule)
        
    def addDeliveryChargeRule(self, deliveryChargeRule):
        self.deliveryChargeRules.append(deliveryChargeRule)
        
    def getProductsRepository(self):
        return self.productsRepository
    
    def setProductsRepository(self, productRepository):
        self.productsRepository = productRepository
        
    def calculateDeliveryCosts(self):
        for deliveryChargeRule in deliveryChargeRules:
            if(not isinstance(deliveryChargeRule, AbstractDeliveryChargeRule)):
                continue
                
            if(deliveryChargeRule.isApplicable()):
                return deliveryChargeRule.getDeliveryCharge()
            
        return 0.0
    
    def calculateDiscount(self):
        discount = 0.0
        for discountRule in discountRules:
            if(not isinstance(discountRule, AbstractDiscountRule)):
                continue
            if(discountRule.isApplicable()):
                discount+=discountRule.getDiscount().getPrice()
                
        return discount
            
        