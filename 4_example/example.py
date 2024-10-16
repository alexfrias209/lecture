import ipdb
import sys
from engine_car import Car, Engine  

def main():
    engine = Engine(300)  
    car = Car("Toyota", "Supra")  

    car.describe()
    print(car)
    print(engine)
    car.start()  

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Exception caught:", e)  
        ipdb.post_mortem()  
