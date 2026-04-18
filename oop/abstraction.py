from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engin(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def colour(self):
        print("you are blue")

class Car(Vehicle):
    def start_engin(self):
        print("Car engine started")
    
    def stop_engine(self):
        print("Car engine stopped")

#usage
car = Car()
car.start_engin() # output: Car engine started
car.colour()