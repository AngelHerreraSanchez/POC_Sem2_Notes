# try:
#     stream = open('C:\\Users\\Nicholas Armstrong\\Development\\POC_Sem2_Notes\\11_Functional Programming\\03_File Handling\\animals.txt')
#     # your code goes here
#     stream.close()
# except Exception as e:
#     print('An error occurred: ', e)

    
# try:
#     stream = open('C:\\Users\\Nicholas Armstrong\\Development\\POC_Sem2_Notes\\11_Functional Programming\\03_File Handling\\animals.txt')
#     print(stream.read())
#     stream.close()
# except Exception as e:
#     print('An error occurred: ', e)
    
# try:
#     stream = open(
#         'C:\\Users\\Nicholas Armstrong\\Development\\POC_Sem2_Notes\\11_Functional Programming\\03_File Handling\\animals.txt')
#     print(stream.read(10))
#     print(stream.read(10))
#     stream.seek(5)
#     print(stream.read(10))
#     stream.close()
# except Exception as e:
#     print('An error occurred: ', e)
    
try:
    stream = open(
        'C:\\Users\\Nicholas Armstrong\\Development\\POC_Sem2_Notes\\11_Functional Programming\\03_File Handling\\newfile.txt', 'w')
    stream.write('This is the first message!\n')
    stream.write('This is the second message!')
    stream.close()
except Exception as e:
    print('An error occurred:', e)
    

    
