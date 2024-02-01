# try:
#     value = int(input('Enter an int: '))
#     print(1/value)
# except:
#     print('Something went wrong')
# else:
#     print('Everything is perfect')
      

def get_inverse(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return None
    finally:
        print('I am always printed!')


# answer = get_inverse(5)
# print(answer)

answer = get_inverse(0)
print(answer)