class Car():
    def __init__(self, model, colour, initial_speed=0):
        self.model = model
        self.colour = colour
        if initial_speed < 0:
            self.__speed = 0
        else:
            self.__speed = initial_speed

    def speed_up(self):
        self.__speed += 5

    def slow_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5

    def show_speed(self):
        print('Current speed:', self.__speed)


my_lovely_car = Car('T-Roc', 'red', -50)
my_lovely_car.speed = -10
my_lovely_car.show_speed()
