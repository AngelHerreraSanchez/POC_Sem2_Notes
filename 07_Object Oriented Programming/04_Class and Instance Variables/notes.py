
# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Dog():
#     counter = 0

#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#         Dog.counter += 1


# my_pet = Dog('Teddy', 2)
# kates_pet = Dog('Foxy', 5)
# adams_pet = Dog('Luna', 1)

# # print(my_pet.counter)
# # print(kates_pet.counter)
# # print(adams_pet.counter)

# print(Dog.counter)
# Dog.counter += 1
# print(Dog.counter)


# class Dog():
#     __counter = 0

#     def get_count():
#         return Dog.__counter

#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#         Dog.__counter += 1

# my_pet = Dog('Teddy', 2)
# kates_pet = Dog('Foxy', 5)
# adams_pet = Dog('Luna', 1)

# print(Dog.get_count())


class MathUtility:
    __pi = 3.14159265358979323646233
    __e = 2.718281828459045
    
    def pi():
        return MathUtility.__pi 
    
    def e():
        return MathUtility.__e
    
    def abs(number):
        if(number < 0):
            return -number
        else:
            return number
      
        
print(MathUtility.pi())
print(MathUtility.e())
print(MathUtility.abs(-5))
            

    





