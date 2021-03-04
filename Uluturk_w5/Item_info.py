'''
Developer: Ömer Ulutürk
Date: 04.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement

---PROJECT---
Define a class named ``ItemInfo` with the following description:
item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item),
net_price(Price after discount)
Methods :
* A member method calculate_discount() to calculate discount as per the following rules:
* If qty <= 10 —> discount is 0
* If qty (11 to 20 inclusive) —> discount is 15
* If qty >= 20 —> discount is 20
* A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
* A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount()
 to calculate the discount and net_price(price * qty - discount).
* A function show_all() or similar name to allow user to view the content of all the data members.
'''


class ItemInfo():
    def __init__(self):
        pass

    def buy(self):
        self.item_code = input("item code:")
        self.item = input("item:")
        self.price = float(input("price:"))
        self.qty = int(input("quantity:"))
        self.net_price = int(input("net price:"))
        self.discount = None


    def calculate_discount(self):
        if self.qty >= 20:
            self.discount = 20
        elif self.qty>11:
            self.discount=15
        else:
            self.discount=0
        self.net_price=self.price*self.qty-self.discount

    def show_all(self):
        print(f"item code:{self.item_code}\nitem:{self.item}\nprice:{self.price}\n"
              f"quantity:{self.qty}\nnet price:{self.net_price}\ndiscount:{self.discount}")
a=ItemInfo()
a.buy()
a.calculate_discount()
a.show_all()
