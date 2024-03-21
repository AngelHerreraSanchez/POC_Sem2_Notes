try:
    stream = open('animals.txt')
    # your code goes here
    stream.close()
except Exception as e:
    print('An error occurred: ', e)

try:
    stream = open('animalsssd.txt')
    # your code goes here
    stream.close()
except Exception as e:
    print('An error occurred: ', e)
    
    try:
    stream = open('animals.txt')
    print(stream.read())
    stream.close()
except Exception as e:
    print('An error occurred: ', e)
    
    try:
    stream = open('animals.txt')
    print(stream.read(10))
    print(stream.read(10))
    stream.close()
except Exception as e:
    print('An error occurred: ', e)
    
try:
    stream = open('newfile.txt', 'w')
    stream.write('This is the first message!\n')
    stream.write('This is the second message!')
    stream.close()
except Exception as e:
    print('An error occurred:', e)
    
try:
    stream = open('newfile.txt', 'w')
    stream.write('This is a brand-new message!')
    stream.close()
except Exception as e:
    print('An error occurred:', e)
    
