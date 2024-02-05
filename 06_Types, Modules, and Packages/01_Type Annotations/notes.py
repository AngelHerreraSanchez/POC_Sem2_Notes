def min(a : int, b : int) -> int:
    print(a.bit_count())
    print(b.bit_count())
    if(a < b):
        return a
    else:
        return b

def print_min(a: int, b: int) -> None:
    print(a.bit_count())
    print(b.bit_count())
    if(a < b):
        print(a)
    else:
        print(b)

number1 : int = int(input("Enter a number"))
number2 : int = int(input("Enter another number"))

