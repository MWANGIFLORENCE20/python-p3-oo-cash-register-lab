#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self,discount=0,total=0):
        self.discount=discount
        self.total=total
        self.items= []
        

    def add_item(self,title,price,Quantity=1):
        self.total += price * Quantity
        self.items.extend([(title)] * Quantity)
       
    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")
        
    def void_last_transaction(self):
            if self.items:
                last_item= self.items.pop()
                self.total-= last_item[1]
            else:
                 self.total = 0.0