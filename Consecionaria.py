#Consecionario de autos 

class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.available_for_rent = True
        self.available_for_sell = True


    def rent(self):
        if self.available_for_rent:
            self.available_for_rent = False
            pr
        else
            