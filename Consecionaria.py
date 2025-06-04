#Consecionario de autos 

class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.available_for_rent = True
        self.available_for_sell = True

    def rent_car(self): 
        if self.available_for_rent:
            self.available_for_rent = False
            print(f"El auto {self.brand}, {self.model} ha sido rentado.")
            return True  # Indica éxito
        else:
            print(f"Lo sentimos, el auto {self.brand}, {self.model} no está disponible para rentar en este momento.")
            return False # Indica fracaso

    def sell_car(self):
        if self.available_for_sell:
            self.available_for_sell = False
            self.available_for_rent = False # Un auto vendido YA NO está disponible para rentar!
            print(f"El auto {self.brand}, {self.model} ha sido vendido.")
            return True  # Indica éxito
        else:
            print(f"Lo sentimos, el auto {self.brand}, {self.model} no está disponible para vender en este momento.")
            return False # Indica fracaso

    def rebuy_car(self):
        self.available_for_sell = True
        self.available_for_rent = True # Un auto recomprado VUELVE a estar disponible para rentar!
        print(f"El auto {self.brand}, {self.model} ha sido devuelto y está disponible para la venta nuevamente.")
        return True  # Indica éxito
    
    
class User:
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname
        self.rented_cars = []
        self.purchased_cars = []

    def rentCar(self, car):
        if car.available_for_rent: # Primero verificas si el auto está disponible
            car.rent_car() # Si está disponible, lo rentas (y esto lo marca como no disponible)
            self.rented_cars.append(car) # Y lo añades a la lista del usuario
            print(f"El usuario {self.name} ha rentado el auto {car.brand}, {car.model}")
        else:
            # Si no estaba disponible, solo imprimes el mensaje de no disponible
            print(f"Lo sentimos, el auto {car.brand}, {car.model} no está disponible para rentar en este momento")
            # No haces nada más, porque el auto no se pudo rentar.

    def buyCar(self, car):
        car.sell_car() 
        if car.available_for_sell:
            self.purchased_cars.append(car)
            print(f"El usuario {self.name} ha comprado el auto {car.brand}, {car.model}")
        else:
            print(f"Lo sentimos, el auto {car.brand}, {car.model} no está disponible para vender en este momento")

class Concesionaria:
    def __init__(self):
        self.cars = []
        self.users = []
        self.rented_cars = []
        self.sold_cars = []
        self.rebuy_cars = []
        
    def addCar(self, car):
        self.cars.append(car)
        print(f"El auto {car.brand}, {car.model} ha sido agregado a la concesionaria")

    def registerUser(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado en la concesionaria")

    def showAvailableCars(self):
        print("Autos disponibles:")
        for car in self.cars:
            if car.available_for_rent or car.available_for_sell:
                print(f"{car.brand}, {car.model}, {car.year}, ${car.price}")


#Register a car
car1 = Car("Toyota", "Corolla", 2020, 20000)
car2 = Car("Honda", "Civic", 2021, 22000)
car3 = Car("Ford", "Focus", 2019, 18000)
car4 = Car("Chevrolet", "Cruze", 2022, 25000)
#Create a user
user1 = User(1, "Juan", "Perez")
user2 = User(2, "Maria", "Gomez")

#Create a dealership
dealership = Concesionaria()
dealership.addCar(car1)
dealership.addCar(car2)
dealership.addCar(car3)
dealership.addCar(car4)

#Show available cars
dealership.showAvailableCars()

#Register users
dealership.registerUser(user1) 
dealership.registerUser(user2)

#Show available cars
dealership.showAvailableCars()

#User rents a car
user1.rentCar(car1)

#User buys a car
user2.buyCar(car2)

#User tries to rent a car that is not available
user1.rentCar(car1)

#User tries to buy a car that is not available
user2.buyCar(car2)

#User returns a car
car1.rebuy_car()  # Rebuying the car makes it available again

#User rents a car again
user1.rentCar(car1)
#User buys a car again
user2.buyCar(car2) 

#Show available cars after transactions
dealership.showAvailableCars()






