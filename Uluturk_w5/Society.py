'''
Developer: Ömer Ulutürk
Date: 04.03.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement

---PROJECT---
Create the class Society with following information:
society_name,house_no_of_mem, flat, income
Methods :
- An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
- input_data() To read information from members
- allocate_flat() To allocate flat according to income using the below table.
- show_data() to display the details of the entire class.
Income	Flat
>=25000	A Type
>=20000 and <25000	B Type
>=15000 and <20000	C Type
<15000	D Type
'''

class Society():
    def __init__(self):
        pass

    def input_data(self):
        self.society_name = input("Please enter society name:")
        self.house_no_of_mem = input("Please enter member's house number:")
        self.income = int(input("Please enter income:"))


    def allocate_flat(self):
        if self.income >=2500:
            self.flat="A Type"
        elif self.income >=2000:
            self.flat ="B Type"
        elif self.income >=1500:
            self.flat ="C Type"
        else:
            self.flat ="D Type"
    def show_data(self):
        print(f"Society name is:{self.society_name}\nHouse no:{self.house_no_of_mem}\nIncome:{self.income}\nFlat:{self.flat}")
s1=Society()
s1.input_data()
s1.allocate_flat()
s1.show_data()





