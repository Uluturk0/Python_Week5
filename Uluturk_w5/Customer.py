'''
Developer: Ömer Ulutürk
Date: 04.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement

---PROJECT---
Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.
Class Items : Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()
calculate_discount():
total_price = price * qty
discount —> 25% if total_price >= 4000
discount —> 15% if total_price >= 2000
discount —> 10% if total_price < 2000
price_tobe_paid = total_price – discount
shopping_cart():
Let user add items in the shopping basket. Be creative with the items, set their prices as well.
__str__():
Print items added and total price nicely. Class Customer : Methods: __init__()``, get_cust_info()this is optional,str()`
Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in __init__() and pass customer information as arguments while creating a customer object.
__str__():
Print customer information and price nicely. Find a way to link two classes. For example, instances of both classes may have a customer number. With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. So Customer class instance holds the customer info, Items class holds the shopped item’s info for the same customer ID number such as price, quantity or so.
In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.
Simple example:
Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]
Crate a few customers and print their information (Personal and shopping info).
'''

class Customer():
    def __init__(self):
        self.name = input("Customer name:")
        self.surname = input("Customer surname:")
        self.customer_id = input("Customer id:")

    def __str__(self):
        return f"Name:{self.name} Surname:{self.surname} ID:{self.customer_id}"


class Items(Customer):
    def __init__(self):
        self.items = []
        self.prices = []


    def shopping_cart(self):
        while True:
            self.item = input("Add your item")
            self.items.append(self.item)
            self.price = int(input("item price: "))
            self.qty = int(input("quantity: "))
            self.prices.append([self.price, self.qty])

            answer = input("Press enter for continue, any key to to exit.")
            if answer == "":
                continue
            else:
                break

    def calculate_discount(self):
        self.price_tobe_paid = 0
        self.total_price = 0
        self.total_discount=0
        for i in self.prices:
            self.total_item_price = i[0] * i[1]
            self.total_price += self.total_item_price

            if self.total_price >= 4000:
                self.discount = self.total_price * 0.25
            elif self.total_price >= 2000:
                self.discount = self.total_price * 0.15
            else:
                self.discount = self.total_price * 0.1

            self.total_discount +=self.discount
        self.price_tobe_paid = self.total_price - self.total_discount

    def __str__(self):
        return f"Item:{self.items} Total Price :{self.total_price} Discount:{self.total_discount} " \
               f"Price to be paid:{self.price_tobe_paid}"

    def get_total_amount(self):
        pass


a = Customer()
b = Items()
b.shopping_cart()
b.calculate_discount()
print(a)
print(b)
