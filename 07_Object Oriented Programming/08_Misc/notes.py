class Vehicle:
    def __init__(self, speed):
        self.speed = speed


class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count


class Car(LandVehicle):
    pass


print(isinstance(my_vehicle, Vehicle))
print(isinstance(my_land_vehicle, Vehicle))
print(isinstance(my_car, Vehicle))

print(isinstance(my_vehicle, LandVehicle))
print(isinstance(my_land_vehicle, LandVehicle))
print(isinstance(my_car, LandVehicle))

print(isinstance(my_vehicle, Car))
print(isinstance(my_land_vehicle, Car))
print(isinstance(my_car, Car))


class Vehicle():
    def go(self):
        print('Going!')


class Flyable():
    def fly(self):
        print('Flying!')


class Airplane(Vehicle, Flyable):
    pass

my_plane = Airplane()
my_plane.go()
my_plane.fly()


class Vehicle():
    def go(self):
        print('Going!')

    def introduce(self):
        print('I am a Vehicle')


class Flyable():
    def fly(self):
        print('Flying!')

    def introduce(self):
        print('I am a Flyable')


class Airplane(Vehicle, Flyable):
    pass


class Vehicle():
    def go(self):
        print('Going!')

    def introduce(self):
        print('I am a Vehicle')


class Flyable():
    def fly(self):
        print('Flying!')

    def introduce(self):
        print('I am a Flyable')


class Airplane(Flyable, Vehicle):
    pass

class Vehicle():
    def show_power_type(self):
        print('I can use power from various sources')

class ElectricVehicle(Vehicle):
    def show_power_type(self):
        print('I can use power from electricity')
        
class PetrolVehicle(Vehicle):
    def show_power_type(self):
        print('I can use power from petrol')

class HybridCar(ElectricVehicle, PetrolVehicle):
    pass


my_toyota_yaris = HybridCar()
my_toyota_yaris.show_power_type()

class Vehicle():
    def show_power_type(self):
        print('I can use power from various sources')

class ElectricVehicle(Vehicle):
    def show_power_type(self):
        print('I can use power from electricity')
        
class PetrolVehicle(Vehicle):
    def show_power_type(self):
        print('I can use power from petrol')

class HybridCar(PetrolVehicle, ElectricVehicle):
    pass


my_toyota_yaris = HybridCar()
my_toyota_yaris.show_power_type()



