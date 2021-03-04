'''
Developer: Ömer Ulutürk
Date: 04.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement

---PROJECT---
Define a class named Product with the following specifications:
Data members:
- product_id – A string to store product.
- product_name - A string to store the name of the product.
- product_purchase_price – A decimal to store the cost price of the product.
- product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
- Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
Methods :
- A constructor to intialize all the data members with valid default values.
- A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
- Margin	Remarks
    <0 (negative)	Loss
    >0 (positive)	Profit
- A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
- A method get_details() that displays all the data members.
'''

class Product():
    def set_details(self):
        self.product_id=input("Product id:")
        self.product_name=input("Product name:")
        self.product_purchase_price=int(input("Purchase price of product:"))
        self.product_sale_price=int(input("Sale price of product:"))

    def set_remarks(self):
        if self.product_sale_price - self.product_purchase_price <0:
            self.margin="Loss"
        elif self.product_sale_price - self.product_purchase_price >0:
            self.margin="Profit"

    def get_details(self):
        print(f"Product id:{self.product_id}\nProduct name:{self.product_name}\n"
              f"Purchase price of product:{self.product_purchase_price}\n"
              f"Sale price of product:{self.product_sale_price}\nMargin:{self.margin}")

a=Product()
a.set_details()
a.set_remarks()
a.get_details()