#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 17:00:52 2022

@author: ajit
"""

class Bill:
    def __init__(self, cn = '', tn = 0, order = ''):
        self.customerName = cn
        self.tableNumber = tn
        self.order = order
        
    def getDetails(self):
        self.customerName = input('Enter customer name:')
        self.tableNumber = int(input('Enter table number:'))
        self.order = input('Enter order:')
        
    def extractDetails(self):
        listItems = self.order.split(',')
        
        ls = []
        for order in listItems:
            single = order.split('x')
            single[1] = int(single[1])
            ls.append(single)
        
        return ls
    
class RestaurantBill(Bill):
    def __init__(self, pl = ''):
        super().getDetails()
        self.priceList =  pl
    
    def totalBill(self):
        listItems = self.priceList.split(',')
        
        priceL = [order.split('-') for order in listItems]
        
        #print(priceL)
        
        priceMap = {}
        for order in priceL:
            priceMap[order[0]] = float(order[1])
        
        
        
        custOrder = self.extractDetails()
        
        
        total = 0
        
        for order in custOrder:
            total+= priceMap[order[0]]*order[1]
        
        return total
    
    def completeBill(self):
        total = self.totalBill()
        
        # 1% GST and 2% service tax.
        return total + total*0.01 + total*0.02

R1 = RestaurantBill('dosa-100,vada-30,idli-25,pongal-23,upma-20') 
print('Total bill: ', R1.totalBill())
print('Complete bill: ', R1.completeBill())       