def calculate_inverse(number):
  assert (number != 0), 'Got 0 as number!'
  return 1/number


number = int(input("Enter a number: "))
print(calculate_inverse(number))
