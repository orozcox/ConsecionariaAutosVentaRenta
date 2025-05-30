#Consecionario de autos 

class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.available_for_rent = True
        self.available_for_sell = True

class User:
    def


    def rent(self):
        if self.available_for_rent:
            self.available_for_rent = False
            print(f"El auto {self.brand}, {self.model} ha sido rentado")
        else:
            