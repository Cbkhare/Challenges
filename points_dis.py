
#In case data is passed as a parameter

from sys import argv
import re
import math
#from itertools import permutations
#from string import ascii_uppercase

file_name = argv[1]
fp = open(file_name,'r+')

#contents = [line.strip('\n').split(' ') for line in fp]

for line in fp:
    strg = str(line)
    #print (strg,type(strg))
    [(x1,y1),(x2,y2)] = re.findall(r'(-?[\d.]+?),\s(-?[\d.]+)', strg)
    #print (x1,y1,x2,y2)

    dis = math.sqrt(pow((int(x1)-int(x2)),2)+pow((int(y1)-int(y2)),2))
    print (int(dis))
                
'''
 You have coordinates of 2 points and need to find the distance between them.
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

(25, 4) (1, -6)
(47, 43) (-25, -11)


All numbers in input are integers between -100 and 100.
Output sample:

Print results in the following way.
26
90

You don't need to round the results you receive. They must be integer numbers.
'''
