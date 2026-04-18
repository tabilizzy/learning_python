class Car:
    def __init__(self, brand: str, model:str):
        self.brand = brand
        self.model = model

    def drive(self):
        return f"this car can drive"


car1 = Car("Toyota", "RVA")

print(car1.brand)
print(car1.model)
print(car1.drive())