class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower


    def start(self):
        print(f"Engine with {self.horsepower} HP is starting...")


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  


    def describe(self):
        print(f"This car is a {self.make} {self.model}.")





