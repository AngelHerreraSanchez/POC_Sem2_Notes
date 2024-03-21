# # # def function_name(parameter1, parameter2):
# # #   #instruction1
# # #   #instruction2

# # # lambda parameter1, parameter2: #instruction

# # def sum(a, b):
# #     return a + b

# # # lambda a, b: a + b

# # # lambda x, y: x + y

# # print(sum(5, 3))

# # another_sum = lambda a, b: a + b

# # print(another_sum(5, 3))

# def apply_func(elements, func):
#     for element in elements:
#         print(func(element))


# def my_func(x): return x * x


# apply_func([1, 2, 3, 4, 5], my_func)


# def my_func(x): return 1/x


# apply_func([1, 2, 3, 4, 5], my_func)


# def my_func(x): return 0


# apply_func([1, 2, 3, 4, 5], my_func)

# apply_func([1, 2, 3, 4, 5], lambda x: x * x * x)

# my_func2 = lambda x: 1 if x else 2

# def printThenReturnSum(x, y):
#     sum = x + y
#     print(sum)
#     return sum

# printThenReturnSumVar = lambda x, y: printThenReturnSum(x, y)

# print(printThenReturnSumVar(3, 4))
