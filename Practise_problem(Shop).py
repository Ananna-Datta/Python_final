class product :
    add=[]
    def __init__(self,name,prize,quantity) -> None:
        self.name=name
        self.prize=prize
        self.quantity=quantity

class shop(product):
    def __init__(self, name, prize, quantity) -> None:
        super().__init__(name, prize, quantity)

    def add_product(self,name):
        x={name}
        self.add.append(x)

    def buy_product(self, buy):
        for i in self.add:
            if i==buy:
                print('Congress')
    

lst=shop('apple',20,2)
lst.add_product('Rice')
lst.add_product('Egg')
lst.add_product('Salt')
print(lst.add)

lst2=shop('apple',20,2)
print(lst2.buy_product('df'))
