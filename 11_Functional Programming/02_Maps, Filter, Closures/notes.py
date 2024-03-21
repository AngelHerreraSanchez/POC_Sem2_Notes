def lambda_func(i): return i * 2
my_func = lambda i: i * 2

initial_list = [1, 2, 3, 4, 5]



# map_result = map(lambda_func, initial_list)
# print(map_result)
# print(next(map_result))
# print(next(map_result))
# print(next(map_result))
# print(next(map_result))
# print(next(map_result))
# print(next(map_result))

# map_result = map(lambda_func, initial_list)
# for element in map_result:
#     print(element, end=',')
    
# map_result = map(lambda_func, initial_list)
# new_list = list(map_result)
# print(new_list)

# map_result = map(my_func, initial_list)
# new_list = list(map_result)
# print(new_list)

# print(list(map(lambda i: i * 2, [1, 2, 3, 4, 5])))

# print(list(filter(lambda i: i % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8])))

# emails = [
#     'frank@gmail.com',
#     'i love python',
#     '98237434',
#     'jonsmith@yahoo.com',
#     'whereareyou@mywebsite.co.uk',
#     'fs3dfss'
# ]
# valid_emails = list(filter(lambda x: '@' in x, emails))
# print(valid_emails)


# def greet(text):

#     def print_greet():
#         print(text)

#     return print_greet


# say_hello = greet('Hello')
# say_hello()


def make_multiply_closure(x):

    def multiply(y):
        return x * y

    return multiply


multiply_5 = make_multiply_closure(5)
multiply_12 = make_multiply_closure(12)

print(multiply_5(10))
print(multiply_5(20))

print(multiply_12(10))
print(multiply_12(20))


