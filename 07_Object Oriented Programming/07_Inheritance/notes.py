class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class Car(LandVehicle):
    pass


issubclass(Car, LandVehicle)

issubclass(LandVehicle, Vehicle)

issubclass(Car, Vehicle)
issubclass(Car, Car)


class Vehicle:
    class_message = 'This is a message from the Vehicle class!'

    def __init__(self, speed):
        self.speed = speed


class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count
        print(super().class_message)


class Car(LandVehicle):
    pass


my_car = Car(50, 4)

my_car.class_message


class Vehicle:
    class_message = 'This is a message from the Vehicle class!'

    def __init__(self, speed):
        self.speed = speed


class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count
        print(super().class_message)

    def speed_up(self):
        self.speed += 5


class Car(LandVehicle):
    def super_speed(self):
        print('Super speed activated!')
        super().speed_up()
        super().speed_up()
        super().speed_up()
        

my_fast_car = Car(10, 4)
print(my_fast_car.__dict__)
my_fast_car.super_speed()
print(my_fast_car.__dict__)
my_fast_car.speed_up()
print(my_fast_car.__dict__)


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class Car(LandVehicle):
    pass


my_car = Car()
print(my_car.__dict__)

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    pass

class Car(LandVehicle):
    pass

my_car = Car(5)
print(my_car.__dict__)


class Vehicle:
    def __init__(self, speed):
        self.speed = speed


class LandVehicle(Vehicle):
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count


class Car(LandVehicle):
    pass

my_car = Car(5)
print(my_car.__dict__)

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count

class Car(LandVehicle):
    pass

my_car = Car(5, 10)
print(my_car.__dict__)

my_car.speed


