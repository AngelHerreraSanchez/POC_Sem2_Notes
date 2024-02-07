import random
import platform


platform.platform()


platform.platform(True, True)
platform.machine()


platform.processor()


platform.system()


platform.python_implementation()


platform.python_version_tuple()


print(random.random())
print(random.random())
print(random.random())

random.seed(0)
print(random.random())
print(random.random())
print(random.random())

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Alan', 'Kate', 'Mary', 'Kate', 'Jo', 'John']

print(random.choice(numbers))
print(random.choice(names))


random.choice('CanYouFeelThePowerOfPython')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10):
    print(random.choice(numbers))

names = ['Alan', 'Kate', 'Mary', 'Kate', 'Jo', 'John']

random.sample(names, 6)


names = ['Alan', 'Kate', 'Mary', 'Kate', 'Jo', 'John']

random.sample(names, 7)
