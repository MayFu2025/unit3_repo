# Inheritance vs Composition

import random

class Engine:
    def __init__(self, fuel_type:str, size:int):
        self.fuel_type = fuel_type
        self.size = size

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class LicensePlate:
    def __init__(self):
        self.license_pate = None

    def set_license(self):
        license = ""
        japanese = ["あ", "い", "う", "え", "お"]
        license += japanese[random.randint(0, 4)]
        for n in range(3):
            license += str(random.randint(0, 9))
        license += "-"
        for n in range(2):
            license += str(random.randint(0, 9))
        self.license_pate = license
        return license

class Vehicle(LicensePlate):
    def __init__(self, brand, model):
        super().__init__()
        self.brand = brand
        self.model = model
        self.engine = None
        self.license_plate = None

    def set_engine(self, engine):
        self.engine = engine

    def start(self):
        if self.engine:
            print(f"{self.brand} {self.model}'s engine is starting.")
            self.engine.start()
        else:
            print("No engine set for the vehicle.")

    def stop(self):
        if self.engine:
            print(f"{self.brand} {self.model}'s engine is stopping.")
            self.engine.stop()
        else:
            print("No engine set for the vehicle.")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors, passenger_cap):
        super().__init__(brand,model)
        self.num_doors = num_doors
        self.passenger_cap = passenger_cap
        self.num_passengers = 0

    def add_passengers(self,nu_add:int):
        if nu_add + self.num_passengers >= self.passenger_cap:
            output = f"No more space. {self.num_passengers}/{self.passenger_cap} people on car."
        else:
            self.num_passengers += nu_add
            output = f"Added passengers. {self.num_passengers}/{self.passenger_cap} people on car."
        return output

    def remove_passengers(self,nu_remove:int):
        if self.num_passengers - nu_remove < 0:
            output = f"Less people on than requested. {self.num_passengers}/{self.passenger_cap} people on car."
        else:
            self.num_passengers -= nu_remove
            output = f"Removed passengers. {self.num_passengers}/{self.passenger_cap} people on car."
        return output

## Task:
electric_engine = Engine("Electric", 100)
new_car = Car(brand="Mitsubishi", model="Lancer", num_doors=4, passenger_cap=4)
new_car.set_engine(electric_engine)

# The datatype of the input engine would be a string
