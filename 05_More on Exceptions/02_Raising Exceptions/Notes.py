# def return_bigger(a, b):
#     if not isinstance(a, int) or not isinstance(b, int):
#         raise ValueError
#     if b > a:
#         return b
#     else:
#         return a


# print(return_bigger(5, 3))


# print(return_bigger(5, 'b'))


# def return_reverse(x):
#     try:
#         return 1/x
#     except:
#         print('Something went wrong')


# return_reverse(0)


def return_reverse(x):
    try:
        return 1/x
    except:
        print('Something went wrong')
        raise

return_reverse(0)
