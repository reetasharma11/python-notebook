import os


file_path = '/home/reeta/Desktop/python-notebook/housing.data'

if os.path.isfile(file_path):
    print('I have a file to process')

else:
    print('Boo,no file for me')


my_file = open(file_path)


for line in my_file:
    print('')

    #list = my_file.readline()
    #listline = list.split() 
    #print(listline)    
           ##### or #####
    print(my_file.readline().split())

my_file.close()










