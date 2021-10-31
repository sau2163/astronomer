# astronomer

Assumptions

The library is fairly simple and is based on the following assumptions:-

1. Delivery is calculated before discounts as applied. 
2. New Special offers/discounts can be added 
3. Prices are stored against products in a given currency to support  multi-currency support.


Usage:

import sys

import os

path_parent_1 = os.path.realpath(r'./')

path_parent_2 = os.path.realpath(r'./Rules/DiscountRule')

path_parent_3 = os.path.realpath(r'./Rules/DeliveryChargeRule')

path_parent_4 = os.path.realpath(r'./Repository')

path_parent_5 = os.path.realpath(r'./Rules')

path_parent_6 = os.path.realpath(r'./Entity')



sys.path.append(path_parent_1)

sys.path.append(path_parent_2)

sys.path.append(path_parent_3)

sys.path.append(path_parent_4)

sys.path.append(path_parent_5)

sys.path.append(path_parent_6)

 

from Basket import Basket

from Currency import Currency

from Colour import Colour

from ProductRepository import ProductRepository

from OrderValueBasedDeliveryChargeRule import OrderValueBasedDeliveryChargeRule

from SecondHalfPriceDiscountRule import SecondHalfPriceDiscountRule

 

 

basket = Basket()

usd = Currency('USD', 'US Dollars', '$')

red = Colour('R', 'Red')

 

repository = ProductRepository()

basket.setProductsRepository(repository)

 

basket.addProduct('G01')

basket.addProduct('B01')

basket.addProduct('R01')

 

basket.addDeliveryChargeRule(0, 50.00, 4.95)

basket.addDiscountRule(SecondHalfPriceDiscountRule

                       (

                       Product('R01', 'Red Widget', red, Price(32.95, usd))   

                      

                      )

                      )

print(basket.calculateDiscount())

print(basket.calculateDeliveryCosts())

print(basket.calculateOrderValueTotal())

print(basket.getGrandTotal())
