try:
    value = int(input('Enter an int: '))
    print(1/value)
except:
    print('Something went wrong')
else:
    print('Eveyrthing is perfect')
    
try:
    value = int(input('Enter an int: '))
    print(1/value)
except:
    print('Something went wrong')
else:
    print('Eveyrthing is perfect')
    

def get_inverse(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return None
    finally:
        print('I am always printed!')


print(get_inverse(5))


print(get_inverse(0))