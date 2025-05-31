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
        print(f"El auto {self.brand}, {self.model} ha sido rentado")
    else:
        print(f"Lo sentimos, el auto {self.brand}, {self.model} no está disponible para rentar en este momento")

    def sell(self):
        pass

class User:
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname






class Concesionaria:
    def __init__(self):
        self.cars = cars[]
        self.users = users[]




