class Wheel:
    def __init__(self, size:int):
        self.size = size

    def get_perimeter(self) -> float:
        return 2*3.14*(self.size/2)

    def get_km_per_rotation(self) -> str:
        return f"{self.get_perimeter() * (2.54 * (10 ** (-5)))} km per rotation"


class Bicycle:
    def __init__(self, wheel:Wheel, material:str):
        self.wheel = wheel
        self.material = material

    def ride(self):
        print(f"Wheel size: {self.wheel.size}, Frame: {self.material}")


MaysWheel = Wheel(26)
MaysBike = Bicycle(MaysWheel, 'aluminum')

MaysBike.ride()
print(MaysBike.wheel.get_km_per_rotation())