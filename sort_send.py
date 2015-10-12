
#In case data is passed as a parameter

from sys import argv
#from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

for line in fp:
    lst = [ round(float(x),3) for x in  line.strip('\n').split(' ')]
    #or use this 
    #lst = ["%.3f" % float(x) for x in  line.strip('\n').split(' ')]
    lst.sort()
    print (str(lst).replace(', ',' ').replace('[','').replace(']',''))


    
'''
contents = [list(map(float,line.strip('\n').split(' '))) for line in fp]
print (contents)
for item in contents:
    item.sort()
    print (str(item).replace(', ',' ').replace('[','').replace(']',''))
'''
