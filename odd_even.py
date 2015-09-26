#In case data is passed as a parameter

from sys import argv
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

contents = [ line.strip('\n') for line in fp]

#print (contents)

for item in contents:

    if int(item)%2 == 0:
        print ('1')
    else:
        print('0')
